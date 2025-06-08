-- procedure to organize the rooms: if the amount of current occupants is greater than the max occupants, then shift around rooms if there is availability in the department. If there is no nurse assigned to a room, then assign if possible

CREATE OR REPLACE PROCEDURE assign_nurses_to_unassigned_rooms()
LANGUAGE plpgsql
AS $$
DECLARE
    cur_room CURSOR FOR
        SELECT r.room_number, r.d_name, r.capacity, COUNT(p.patient_id) AS occupancy
        FROM room r
        LEFT JOIN patient p ON r.room_number = p.room_number AND r.d_name = p.d_name
        GROUP BY r.room_number, r.d_name, r.capacity;

    rec_room RECORD;
    nurse_id INT;
    extra_patients INT;
    cur_patient RECORD;
    alt_room INT;
BEGIN
    OPEN cur_room;
    LOOP
        FETCH cur_room INTO rec_room;
        EXIT WHEN NOT FOUND;

        -- Assign a nurse if none is assigned yet
        IF NOT EXISTS (
            SELECT 1 FROM nurse_room nr
            WHERE nr.room_number = rec_room.room_number AND nr.d_name = rec_room.d_name
        ) THEN
            SELECT employee_id INTO nurse_id
            FROM nurse
            WHERE d_name = rec_room.d_name
            LIMIT 1;

            IF nurse_id IS NOT NULL THEN
                INSERT INTO nurse_room(nurse_id, room_number, d_name)
                VALUES (nurse_id, rec_room.room_number, rec_room.d_name);
            ELSE
                RAISE NOTICE 'No nurse available for room % in department %.',
                    rec_room.room_number, rec_room.d_name;
            END IF;
        END IF;

        -- Check for over-occupancy
        IF rec_room.occupancy > rec_room.capacity THEN
            extra_patients := rec_room.occupancy - rec_room.capacity;

            -- Fetch extra patients to move
            FOR cur_patient IN
                SELECT patient_id, person_id FROM patient
                WHERE room_number = rec_room.room_number AND d_name = rec_room.d_name
                ORDER BY admission_date DESC
                LIMIT extra_patients
            LOOP
                -- Find another room in same department with available space
                SELECT available_room.room_number INTO alt_room
                FROM (
                    SELECT r.room_number, r.capacity, COUNT(p.patient_id) AS current_occupancy
                    FROM room r
                    LEFT JOIN patient p ON r.room_number = p.room_number AND r.d_name = p.d_name
                    WHERE r.d_name = rec_room.d_name
                      AND r.room_number != rec_room.room_number
                    GROUP BY r.room_number, r.capacity
                    HAVING COUNT(p.patient_id) < r.capacity
                    ORDER BY r.capacity - COUNT(p.patient_id) DESC
                    LIMIT 1
                ) AS available_room;

                IF alt_room.room_number IS NOT NULL THEN
                    -- Move patient to alternative room
                    UPDATE patient
                    SET room_number = alt_room.room_number
                    WHERE patient_id = cur_patient.patient_id;

                    RAISE NOTICE 'Moved patient % to room % in department %.',
                        cur_patient.patient_id, alt_room.room_number, rec_room.d_name;
                ELSE
                    RAISE NOTICE 'No alternative room with space found for patient % in department %.',
                        cur_patient.patient_id, rec_room.d_name;
                END IF;
            END LOOP;
        END IF;
    END LOOP;
    CLOSE cur_room;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'An error occurred: %', SQLERRM;
END;
$$;

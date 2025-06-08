-- Call the function get_room_occupancy_info and send out a notice with all the info. Then, call the procedure assign_nurses_to_unassigned_rooms to try and make order

DO $$
DECLARE
    room_cur REFCURSOR;
    rec RECORD;
BEGIN
    -- Call function to get the refcursor
    room_cur := get_room_occupancy_info();

    -- Fetch all from the cursor and print room info
    LOOP
        FETCH room_cur INTO rec;
        EXIT WHEN NOT FOUND;
        RAISE NOTICE 'Room % in Dept %: Capacity=%, Occupancy=%, Nurse Assigned=%',
            rec.room_number, rec.d_name, rec.capacity, rec.current_occupancy, rec.nurse_assigned;
    END LOOP;
    CLOSE room_cur;

    -- Call the procedure to assign nurses and move patients
    CALL assign_nurses_to_unassigned_rooms();

    RAISE NOTICE 'Nurses assigned and patients shifted if needed.';
END;
$$ LANGUAGE plpgsql;

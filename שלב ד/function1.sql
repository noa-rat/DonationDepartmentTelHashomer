-- function that returns the information pertaining to a specific room: its department, maximum occupancy, current occupancy, and true/false if a nurse is assigned to it

CREATE OR REPLACE FUNCTION get_room_occupancy_info()
RETURNS REFCURSOR AS $$
DECLARE
    ref refcursor := 'room_cursor';
BEGIN
    OPEN ref FOR
    SELECT 
        r.room_number,
        r.d_name,
        r.capacity,
        COUNT(p.patient_id) AS current_occupancy,
        CASE 
            WHEN EXISTS (
                SELECT 1 FROM nurse_room nr 
                WHERE nr.room_number = r.room_number AND nr.d_name = r.d_name
            )
            THEN TRUE ELSE FALSE 
        END AS nurse_assigned
    FROM room r
    LEFT JOIN patient p 
        ON p.room_number = r.room_number AND p.d_name = r.d_name
    GROUP BY r.room_number, r.d_name, r.capacity;

    RETURN ref;
END;
$$ LANGUAGE plpgsql;

BEGIN;

-- Step 1: Call the function to open the cursor
SELECT get_room_occupancy_info();

-- Step 2: Fetch data from the returned cursor
FETCH ALL IN room_cursor;  -- Or use the name if you used a named cursor

COMMIT;

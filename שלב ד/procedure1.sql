CREATE OR REPLACE PROCEDURE create_fundraisingEvent_for_department(dept_name VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE
    new_event_id INT;
    fundraiser_id INT;
    proposed_date DATE := CURRENT_DATE + INTERVAL '1 month';
    proposed_location VARCHAR;
BEGIN
    RAISE NOTICE 'Handling department: %', dept_name;

    -- נסה למצוא תאריך ומיקום פנויים בלולאה
    LOOP
        -- מצא מיקום פנוי בחודש הבא
        SELECT l.location_name INTO proposed_location
        FROM (
            SELECT DISTINCT e_location AS location_name
            FROM fundraisingEvent
            WHERE e_location IS NOT NULL
        ) l
        WHERE NOT EXISTS (
            SELECT 1
            FROM fundraisingEvent fe
            WHERE fe.e_date = proposed_date
              AND fe.e_location = l.location_name
        )
        LIMIT 1;

        -- אם נמצא מיקום פנוי – צא מהלולאה
        IF proposed_location IS NOT NULL THEN
            EXIT;
        END IF;

        -- אחרת – עבור לשבוע הבא
        proposed_date := proposed_date + INTERVAL '7 day';

        -- תנאי עצירה: לא לחפש מעבר לחצי שנה קדימה
        IF proposed_date > CURRENT_DATE + INTERVAL '6 month' THEN
            RAISE EXCEPTION 'No available location for department % within a year', dept_name;
        END IF;
    END LOOP;

    -- צור את האירוע
    INSERT INTO fundraisingEvent (e_date, e_name, e_location)
    VALUES (proposed_date, 'Auto-generated event for department ' || dept_name, proposed_location)
    RETURNING e_id INTO new_event_id;

    -- מצא מגייס שאינו מארגן אירוע אחר
    SELECT f.employee_id INTO fundraiser_id
    FROM fundraiser f
    WHERE NOT EXISTS (
        SELECT 1 FROM organizes o
        WHERE o.fundraiser_id = f.employee_id
    )
    LIMIT 1;

    -- אם לא נמצא מגייס
    IF fundraiser_id IS NULL THEN
        RAISE EXCEPTION 'No available fundraiser to assign to department %', dept_name;
    END IF;

    -- קישור המגייס לארגון האירוע
    INSERT INTO organizes (fundraiser_id, e_id)
    VALUES (fundraiser_id, new_event_id);

    RAISE NOTICE 'Created event % on % at % for department %, assigned to fundraiser %',
        new_event_id, proposed_date, proposed_location, dept_name, fundraiser_id;
END;
$$;

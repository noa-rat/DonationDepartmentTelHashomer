-- תוכנית ראשית - יצירת אירועים עבור מחלקות שלא הגיעו ליעד
DO $$
DECLARE
    dept RECORD;
    count_departments INT := 0;
BEGIN
    RAISE NOTICE 'Starting donation check and event creation...';

    FOR dept IN SELECT * FROM get_departments_below_budget() LOOP
        count_departments := count_departments + 1;
        RAISE NOTICE 'Handling department: %', dept.department_name;
        CALL create_fundraisingEvent_for_department(dept.department_name);
        COMMIT;
    END LOOP;

    IF count_departments = 0 THEN
        RAISE NOTICE 'All departments have reached their fundraising goals.';
    ELSE
        RAISE NOTICE 'Processed % departments with unmet fundraising goals.', count_departments;
    END IF;
END $$;

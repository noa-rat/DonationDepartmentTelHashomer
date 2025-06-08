CREATE OR REPLACE FUNCTION get_departments_below_budget()
RETURNS TABLE (
    department_name VARCHAR,
    total_donations NUMERIC,
    required_budget NUMERIC
) AS $$
DECLARE
    rec_dept RECORD;
    total_donations NUMERIC;
BEGIN
    FOR rec_dept IN SELECT d_name, d_yearly_budget, d_funds_allocated FROM department LOOP

        -- Calculate total donations for current year
        SELECT COALESCE(SUM(d.d_amount), 0)
        INTO total_donations
        FROM donation d
        JOIN towards t ON d.donation_id = t.donation_id AND d.donor_id = t.donor_id
        WHERE t.d_name = rec_dept.d_name
          AND EXTRACT(YEAR FROM d.d_date) = EXTRACT(YEAR FROM CURRENT_DATE);

        -- Return row if donations are below expected budget
        IF total_donations < (rec_dept.d_yearly_budget - rec_dept.d_funds_allocated) THEN
            department_name := rec_dept.d_name;
            required_budget := rec_dept.d_yearly_budget - rec_dept.d_funds_allocated;
            get_departments_below_budget.total_donations := total_donations;
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

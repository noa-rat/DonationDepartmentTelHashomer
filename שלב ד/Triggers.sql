-- =============== | Trigger #1a | ========================

-- When adding a new patient, automatically assign a doctor to them. The doctor cannot go over his maximum amount of patients - this depends on the doctor's title and is based on a new table added which maps each type of doctor with their maximum amount of potential patients (table called maximum_amount_of_patients)

CREATE OR REPLACE FUNCTION assign_doctor_to_patient()
RETURNS TRIGGER AS $$
DECLARE
    assigned_doctor_id INT;
BEGIN
    SELECT d.employee_id
    INTO assigned_doctor_id
    FROM doctor d
    JOIN maximum_amount_of_patients m ON d.title = m.type_of_doctor
    WHERE d.d_name = NEW.d_name
    AND (
        SELECT COUNT(*)
        FROM patient p
        WHERE p.doctor_id = d.employee_id
          AND (p.release_date IS NULL OR p.release_date >= CURRENT_DATE)
    ) < m.max_patients
    LIMIT 1;

    IF assigned_doctor_id IS NULL THEN
        RAISE EXCEPTION 'No doctor available in department % with available capacity.', NEW.d_name;
    END IF;

    NEW.doctor_id := assigned_doctor_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_assign_doctor
BEFORE INSERT ON patient
FOR EACH ROW
EXECUTE FUNCTION assign_doctor_to_patient();

CREATE TRIGGER trg_assign_doctor_mother
BEFORE INSERT ON mother
FOR EACH ROW
EXECUTE FUNCTION assign_doctor_to_patient();

CREATE TRIGGER trg_assign_doctor_baby
BEFORE INSERT ON baby
FOR EACH ROW
EXECUTE FUNCTION assign_doctor_to_patient();

-- =============== | Trigger #1b | ========================
-- When a new patient is added, automatically assing them a room in their department which has not yet reached its maximum capacity
CREATE OR REPLACE FUNCTION assign_room_to_patient()
RETURNS TRIGGER AS $$
DECLARE
    assigned_room_number INT;
BEGIN
    SELECT r.room_number
    INTO assigned_room_number
    FROM room r
    WHERE r.d_name = NEW.d_name
    AND (
        SELECT COUNT(*)
        FROM patient p
        WHERE p.room_number = r.room_number
          AND (p.release_date IS NULL OR p.release_date >= CURRENT_DATE)
    ) < r.capacity
    LIMIT 1;

    IF assigned_room_number IS NULL THEN
        RAISE EXCEPTION 'No room available in department % with available capacity.', NEW.d_name;
    END IF;

    NEW.room_number := assigned_room_number;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_assign_room_baby
BEFORE INSERT ON baby
FOR EACH ROW
EXECUTE FUNCTION assign_room_to_patient();

CREATE TRIGGER trg_assign_room_mother
BEFORE INSERT ON mother
FOR EACH ROW
EXECUTE FUNCTION assign_room_to_patient();

CREATE TRIGGER trg_assign_room_mother
BEFORE INSERT ON mother
FOR EACH ROW
EXECUTE FUNCTION assign_room_to_patient();

-- =============== | Trigger #2 | ========================

-- When a new row in the prescription table is added (meaning a patient has been given a prescription of medicine), decrease the stock of that medicine.
CREATE OR REPLACE FUNCTION decrease_stock()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE medicine
    SET stock = stock - 1
    WHERE medicine_id = NEW.medicine_id;

    RETURN NEW; -- You must return NEW in a BEFORE or AFTER INSERT trigger
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_decrease_stock
BEFORE INSERT ON prescription
FOR EACH ROW
EXECUTE FUNCTION decrease_stock();


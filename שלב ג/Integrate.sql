-- add all the new tables

alter table staffmember rename to fundraiser;
alter table fundraiser rename to fundraiser_old;
alter table doctor rename to doctor_old;
alter table nurse rename to nurse_old;
alter table mother rename to mother_old;
alter table baby rename to baby_old;
alter table donor rename to donor_old;
alter table towards rename to towards_old;


-- Revised and cleaned-up integrated DSD with corrected inheritance and hierarchy

CREATE TABLE Person (
  person_id INT PRIMARY KEY,
  name VARCHAR(50),
  p_phone VARCHAR(15),
  p_email VARCHAR(50) UNIQUE,
  p_address VARCHAR(50),
  p_city VARCHAR(50),
  p_country VARCHAR(50)
);

CREATE TABLE StaffMember (
  employee_id INT UNIQUE NOT NULL,
  salary NUMERIC(5,2) NOT NULL,
  title VARCHAR(200) NOT NULL,
  d_name VARCHAR NOT NULL,
  PRIMARY KEY (person_id),
  FOREIGN KEY (d_name) REFERENCES department(d_name)
) INHERITS (Person);

ALTER TABLE StaffMember
  ADD CONSTRAINT staff_empid_unique UNIQUE(employee_id);


CREATE TABLE fundraiser (
  PRIMARY KEY (person_id, employee_id),
  FOREIGN KEY (employee_id) REFERENCES StaffMember(employee_id)
) INHERITS (StaffMember);

CREATE TABLE doctor (
  medical_license_num INT UNIQUE NOT NULL,
  specialization VARCHAR(100) NOT NULL,
  PRIMARY KEY (person_id, employee_id),
  FOREIGN KEY (employee_id) REFERENCES StaffMember(employee_id)
) INHERITS (StaffMember);

CREATE TABLE nurse (
  nursing_license_num INT UNIQUE NOT NULL,
  PRIMARY KEY (person_id, employee_id),
  FOREIGN KEY (person_id) REFERENCES StaffMember(person_id)
) INHERITS (StaffMember);

-- Rename the existing column
ALTER TABLE room RENAME COLUMN current_occupacity TO current_occupancy;

-- Add new column for department name
ALTER TABLE room
ADD COLUMN d_name VARCHAR NOT NULL DEFAULT 'Maternity Ward';

ALTER TABLE mother_old DROP CONSTRAINT IF EXISTS mother_room_number_fkey;
ALTER TABLE nurse_room DROP CONSTRAINT IF EXISTS nurse_room_room_number_fkey;


-- Drop existing primary key if needed
ALTER TABLE room DROP CONSTRAINT room_pkey;

-- Add composite primary key
ALTER TABLE room ADD PRIMARY KEY (room_number, d_name);

-- add maternity ward to department
insert into department (d_name, d_email, d_phone, d_funds_allocated, d_yearly_budget)
VALUES('Maternity Ward', 'maternity@telhashomer.org', '0298647386', 600000, 1000000);

-- Add foreign key to department
ALTER TABLE room ADD CONSTRAINT fk_room_department
  FOREIGN KEY (d_name) REFERENCES department(d_name);

-- Make sure doctor.person_id is a unique foreign key referencing Person
ALTER TABLE doctor
ADD CONSTRAINT doctor_person_id_unique UNIQUE (person_id);

ALTER TABLE doctor
ADD CONSTRAINT doctor_employee_id_unique UNIQUE (employee_id);

CREATE TABLE patient (
  patient_id INT UNIQUE NOT NULL,
  dob DATE NOT NULL,
  blood_type CHAR(3) NOT NULL,
  admission_date DATE NOT NULL,
  release_date DATE,
  weight NUMERIC(5,2) NOT NULL,
  height NUMERIC(5,2) NOT NULL,
  room_number INT NOT NULL,
  d_name VARCHAR NOT NULL,
  doctor_id INT,
  PRIMARY KEY (person_id, patient_id),
  FOREIGN KEY (d_name) REFERENCES department(d_name),
  FOREIGN KEY (room_number, d_name) REFERENCES room(room_number, d_name),
  FOREIGN KEY (doctor_id) REFERENCES doctor(employee_id)
) INHERITS (Person);

-- Ensure the employee_id in the fundraiser table is unique
ALTER TABLE fundraiser
ADD CONSTRAINT fundraiser_employee_id_unique UNIQUE (employee_id);


CREATE TABLE donor (
  donor_id INT UNIQUE NOT NULL,
  is_member BOOLEAN NOT NULL,
  d_type VARCHAR(50) NOT NULL,
  fundraiser_id INT,
  PRIMARY KEY (person_id),
  FOREIGN KEY (fundraiser_id) REFERENCES fundraiser(employee_id)
) INHERITS (Person);

CREATE TABLE mother (
  rooming_in BOOLEAN NOT NULL,
  delivery_type VARCHAR(20) NOT NULL,
  PRIMARY KEY (person_id, patient_id),
  FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
) INHERITS (patient);

-- Ensure person_id in mother table is unique
ALTER TABLE mother
ADD CONSTRAINT mother_person_id_unique UNIQUE (person_id);

ALTER TABLE mother
ADD CONSTRAINT mother_mother_id_unique UNIQUE (patient_id);


CREATE TABLE baby (
  health_status VARCHAR(100) NOT NULL,
  mother_id INT NOT NULL,
  PRIMARY KEY (person_id, patient_id),
  FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
  FOREIGN KEY (mother_id) REFERENCES mother(patient_id)
) INHERITS (patient);

-- Step 1: Create the sequence
CREATE SEQUENCE staffmember_employee_id_seq
  START 1
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 2147483647
  CACHE 1;

-- Step 2: Set the default value of employee_id to the sequence
ALTER TABLE StaffMember
ALTER COLUMN employee_id SET DEFAULT nextval('staffmember_employee_id_seq');

CREATE SEQUENCE person_person_id_seq
  START 1
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 2147483647
  CACHE 1;

-- Step 2: Set the default value of employee_id to the sequence
ALTER TABLE person
ALTER COLUMN person_id SET DEFAULT nextval('person_person_id_seq');

-- increase size of salary
ALTER TABLE StaffMember
ALTER COLUMN salary TYPE NUMERIC(7,2);

-- migrate data in person, staffmember, and doctor from doctor_old

ALTER TABLE doctor DROP CONSTRAINT doctor_employee_id_fkey;


INSERT INTO doctor (
  person_id,
  name,
  p_phone,
  p_email,
  p_address,
  p_city,
  p_country,
  salary,
  title,
  d_name,
  medical_license_num,
  specialization
)
SELECT
  doctor_id,  -- Or use DEFAULT if person_id is serial
  CONCAT(first_name, ' ', last_name),
  phone,
  CONCAT(first_name, ' ', last_name, '@telhashomer.org') AS p_email,
  NULL,  -- address
  NULL,  -- city
  NULL,  -- country
  ROUND((12000 + RANDOM() * (80000 - 20000))::numeric, 2),
  CASE FLOOR(RANDOM() * 7)::INT
        WHEN 0 THEN 'doctor'
        WHEN 1 THEN 'surgeon'
		WHEN 2 THEN 'head doctor'
		WHEN 3 THEN 'attending'
		WHEN 4 THEN 'resident'
		WHEN 5 THEN 'trainee'
        ELSE 'on-call'
   END,
  'Maternity Ward',  -- department
  medical_license_num,
  specialization
FROM doctor_old;

ALTER TABLE nurse DROP CONSTRAINT nurse_person_id_fkey;

INSERT INTO nurse (
  person_id,
  name,
  p_phone,
  p_email,
  p_address,
  p_city,
  p_country,
  salary,
  title,
  d_name,
  nursing_license_num
)
SELECT
  nurse_id,
  CONCAT(first_name, ' ', last_name),
  phone,
  CONCAT(first_name, ' ', last_name, '@telhashomer.org') AS p_email,
  NULL,  -- address
  NULL,  -- city
  NULL,  -- country
  ROUND((12000 + RANDOM() * (40000 - 12000))::numeric, 2),
  CASE FLOOR(RANDOM() * 3)::INT
        WHEN 0 THEN 'nurse'
        WHEN 1 THEN 'head nurse'
        ELSE 'night nurse'
   END,
  'Maternity Ward',  -- department
  nursing_license_num
FROM nurse_old;

insert into department (d_name, d_email, d_phone, d_funds_allocated, d_yearly_budget)
VALUES('Donations Department', 'donations@telhashomer.org', '0894762938', 14000, 18000);

-- create sequence for person_id if need to create more
CREATE SEQUENCE person_id_seq
START WITH 1
INCREMENT BY 1
MINVALUE 1
MAXVALUE 1000000
CYCLE;  -- Optionally, if you want the sequence to reset after reaching the max value.

-- start above the maximum
SELECT MAX(person_id) FROM person;
SELECT setval('person_id_seq', 10000, true);

-- create a table to map the s_id's that already exist as a person_id
CREATE TABLE s_id_map (
    old_id INT PRIMARY KEY,
    new_id INT UNIQUE NOT NULL
);

-- choose new values based on the next available option in person
INSERT INTO s_id_map (old_id, new_id)
SELECT old_id, nextval('person_id_seq')
FROM (
    SELECT s_id AS old_id
    FROM fundraiser_old
    WHERE s_id IN (SELECT person_id FROM person)
) AS conflicts;

-- disable foreign key constraints to change the id's
ALTER TABLE organizes DISABLE TRIGGER ALL;
ALTER TABLE donor_old DISABLE TRIGGER ALL;

-- Update relevant tables with new s_id's
UPDATE organizes p
SET s_id = d_new.new_id
FROM s_id_map d_new
WHERE p.s_id = d_new.old_id;

UPDATE donor_old p
SET s_id = d_new.new_id
FROM s_id_map d_new
WHERE p.s_id = d_new.old_id;

-- enable the disabled constraints
ALTER TABLE organizes ENABLE TRIGGER ALL;
ALTER TABLE donor_old ENABLE TRIGGER ALL;

-- update fundraiser_old with the new s_id's
UPDATE fundraiser_old n
SET s_id = m_new.new_id
FROM s_id_map m_new
WHERE n.s_id = m_new.old_id;

-- increase salary
ALTER TABLE staffmember
ALTER COLUMN salary TYPE NUMERIC(10, 2);

-- drop FK constraint (it's wrong)
ALTER TABLE fundraiser DROP CONSTRAINT fundraiser_employee_id_fkey;

-- migrate data from fundraiser
INSERT INTO fundraiser (
  person_id,
  name,
  p_phone,
  p_email,
  p_address,
  p_city,
  p_country,
  salary,
  title,
  d_name
)
SELECT
  s_id,
  CONCAT(first_name, ' ', last_name),
  s_phone,
  s_email,
  NULL,  -- address
  NULL,  -- city
  NULL,  -- country
  salary,
  position,
  'Donations Department'  -- department
FROM fundraiser_old;

-- MOTHER MIGRATION

-- create a table that contains all the mother_id's that need to be changed and what they're changed to
CREATE TABLE mother_id_map (
    old_id INT PRIMARY KEY,
    new_id INT UNIQUE NOT NULL
);

-- choose the new values
INSERT INTO mother_id_map (old_id, new_id)
SELECT old_id, nextval('person_id_seq')
FROM (
    SELECT mother_id AS old_id
    FROM mother_old
    WHERE mother_id IN (SELECT person_id FROM person)
) AS conflicts;

-- disable constraints of the baby table
ALTER TABLE baby_old DISABLE TRIGGER ALL;

-- Update baby table with new mother_id's
UPDATE baby_old b
SET mother_id = m_new.new_id
FROM mother_id_map m_new
WHERE b.mother_id = m_new.old_id;

-- disable constraints for prescription
ALTER TABLE prescription DISABLE TRIGGER ALL;

-- Update prescription table with new mother_id's
UPDATE prescription p
SET mother_id = m_new.new_id
FROM mother_id_map m_new
WHERE p.mother_id = m_new.old_id;

-- set the new mother_id's
UPDATE mother_old m
SET mother_id = m_new.new_id
FROM mother_id_map m_new
WHERE m.mother_id = m_new.old_id;

-- create a sequence for patient_ids
CREATE SEQUENCE patient_patient_id_seq
  START 1
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 2147483647
  CACHE 1;

ALTER TABLE patient
ALTER COLUMN patient_id SET DEFAULT nextval('patient_patient_id_seq');

alter table mother drop constraint mother_patient_id_fkey;

-- migrate the mothers
INSERT INTO mother (
  person_id,
  name,
  p_phone,
  p_email,
  p_address,
  p_city,
  p_country,
  admission_date,
  dob,
  blood_type,
  weight,
  doctor_id,
  room_number,
  release_date,
  height,
  d_name,
  delivery_type,
  rooming_in
)
SELECT
  b.mother_id,
  CONCAT(first_name, ' ', last_name),
  NULL,
  NULL,
  NULL,  -- address
  NULL,  -- city
  NULL,  -- country
  b.admission_date,
  b.birth_date,
  b.blood_type,
  b.weight,
  (SELECT employee_id
  FROM doctor
  ORDER BY RANDOM()
  LIMIT 1),
  b.room_number,
  b.admission_date + (TRUNC(3 + RANDOM() * 13)::INT || ' days')::INTERVAL,
  ROUND((150 + RANDOM() * 30)::NUMERIC, 1),  -- Height: 45cm to 55cm   
  'Maternity Ward',
  b.delivery_type,
  b.rooming_in
FROM mother_old b;

-- BABY MIGRATION

CREATE TABLE baby_id_map (
    old_id INT PRIMARY KEY,
    new_id INT UNIQUE NOT NULL
);

-- choose the new values
INSERT INTO baby_id_map (old_id, new_id)
SELECT old_id, nextval('person_id_seq')
FROM (
    SELECT baby_id AS old_id
    FROM baby_old
    WHERE baby_id IN (SELECT person_id FROM person)
) AS conflicts;

UPDATE baby_old m
SET baby_id = m_new.new_id
FROM baby_id_map m_new
WHERE m.baby_id = m_new.old_id;

alter table baby drop constraint baby_patient_id_fkey;
alter table baby drop constraint baby_mother_id_fkey1;



INSERT INTO baby (
  person_id,
  name,
  p_phone,
  p_email,
  p_address,
  p_city,
  p_country,
  admission_date,
  dob,
  blood_type,
  weight,
  doctor_id,
  room_number,
  release_date,
  height,
  d_name,
  health_status,
  mother_id
)
SELECT
  b.baby_id,
  NULL,
  NULL,
  NULL,
  NULL,  -- address
  NULL,  -- city
  NULL,  -- country
  b.birth_date,
  b.birth_date,
  b.blood_type,
  b.weight,
  (SELECT doctor_id
  FROM doctor
  ORDER BY RANDOM()
  LIMIT 1),
  m.room_number,
  CASE
        WHEN m.release_date IS NULL THEN NULL  -- If mother release date is NULL, baby release date is also NULL
        WHEN RANDOM() > 0.2 THEN m.release_date  -- 80% chance the baby release date is the same as mother's
        ELSE m.release_date + ((RANDOM() * 60)::INT || ' days')::INTERVAL  -- 20% chance baby's release date is 0 to 60 days after the mother's
    END AS release_date,
  ROUND((45 + RANDOM() * 10)::NUMERIC, 1),  -- Height: 45cm to 55cm   
  'Maternity Ward',
  b.health_status,
  b.mother_id
FROM baby_old b join mother_old m on b.mother_id = m.mother_id;


-- DONOR MIGRATION

CREATE TABLE donor_id_map_final (
    old_id INT PRIMARY KEY,
    new_id INT NOT NULL
);

INSERT INTO donor_id_map_final (old_id, new_id)
SELECT old_id, nextval('person_id_seq')
FROM (
    SELECT donor_id AS old_id
    FROM donor_old
    WHERE donor_id IN (SELECT person_id FROM person)
) AS conflicts;

ALTER TABLE donation DISABLE TRIGGER ALL;

UPDATE donation d
SET donor_id = dm.new_id
FROM donor_id_map_final dm
WHERE d.donor_id = dm.old_id;

ALTER TABLE donation ENABLE TRIGGER ALL;

ALTER TABLE participates_in DISABLE TRIGGER ALL;
-- participates_in FK of donor_id
UPDATE participates_in d
SET donor_id = dm.new_id
FROM donor_id_map_final dm
WHERE d.donor_id = dm.old_id;

ALTER TABLE participates_in ENABLE TRIGGER ALL;

ALTER TABLE towards DISABLE TRIGGER ALL;

-- towards FK of donor_id
UPDATE towards d
SET donor_id = dm.new_id
FROM donor_id_map_final dm
WHERE d.donor_id = dm.old_id;

ALTER TABLE towards ENABLE TRIGGER ALL;


UPDATE donor_old m
SET donor_id = m_new.new_id
FROM donor_id_map_final m_new
WHERE m.donor_id = m_new.old_id;

-- increase the size of name of person
ALTER TABLE person
ALTER COLUMN name TYPE VARCHAR(100); 

ALTER TABLE person
ALTER COLUMN p_address TYPE VARCHAR(100); 

ALTER TABLE person
ALTER COLUMN p_phone TYPE VARCHAR(100); 

ALTER TABLE person
ALTER COLUMN p_city TYPE VARCHAR(100); 

ALTER TABLE person
ALTER COLUMN p_country TYPE VARCHAR(100); 

ALTER TABLE person
ALTER COLUMN p_email TYPE VARCHAR(100); 

alter table donor drop constraint donor_fundraiser_id_fkey;

INSERT INTO donor (
  person_id,
  name,
  p_phone,
  p_email,
  p_address,
  p_city,
  p_country,
  donor_id,
  is_member,
  d_type,
  fundraiser_id
)
SELECT
  donor_id,
  don_name,
  don_phone,
  don_email,
  address, 
  city,  
  country, 
  donor_id,
  is_member,
  d_type,
  s_id
FROM donor_old;

-- Add foreign keys that may not exist yet:
ALTER TABLE staffmember
ADD CONSTRAINT fk_employee_department
FOREIGN KEY (d_name)
REFERENCES department(d_name);

ALTER TABLE prescription RENAME COLUMN mother_id TO patient_id;

-- change person_id to be the patient_id in prescription
UPDATE prescription
SET patient_id = n.patient_id
FROM patient n
WHERE prescription.patient_id = n.person_id;

-- patient index workaround because of issue that inheritance does not support foreign keys
-- add a new table to index all the patient_ids
CREATE TABLE patient_index (
    patient_id INTEGER PRIMARY KEY
);
-- Insert all mother IDs
INSERT INTO patient_index (patient_id)
SELECT patient_id FROM mother;

-- Insert all baby IDs
INSERT INTO patient_index (patient_id)
SELECT patient_id FROM baby;

-- create a function that adds patient_id to the patient_index table
CREATE FUNCTION add_patient_to_index()
RETURNS TRIGGER AS $$
BEGIN
    -- Insert the id from a newly inserted record into the patient_index table
    INSERT INTO patient_index(patient_id) VALUES (NEW.patient_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- create triggers for the insert command on table mother and baby
CREATE TRIGGER add_patient_index_mother
AFTER INSERT ON mother
FOR EACH ROW EXECUTE FUNCTION add_patient_to_index();

CREATE TRIGGER add_patient_index_baby
AFTER INSERT ON baby
FOR EACH ROW EXECUTE FUNCTION add_patient_to_index();

-- create function for deleting the patient_id from the patient_index TABLE
CREATE FUNCTION remove_patient_from_index()
RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM patient_index WHERE patient_id = OLD.id;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- create triggers for the delete command on table mother and baby
CREATE TRIGGER remove_patient_index_mother
AFTER DELETE ON mother
FOR EACH ROW EXECUTE FUNCTION remove_patient_from_index();

CREATE TRIGGER remove_patient_index_baby
AFTER DELETE ON baby
FOR EACH ROW EXECUTE FUNCTION remove_patient_from_index();

-- add foreign key that connects patient_id of prescription to patient_id of patient_index
ALTER TABLE prescription
ADD CONSTRAINT fk_prescription_patient_it
FOREIGN KEY (patient_id)
REFERENCES patient_index(patient_id);

-------------------- | Constraint Handling |----------------------------------

-- ORGANIZES

-- drop the current constraints in organizes so we can reset data
ALTER TABLE organizes
DROP CONSTRAINT organizes_s_id_fkey;

alter table organizes rename column s_id to fundraiser_id;

-- reset the fundraiser_id's to correspond to the new fundraisers
UPDATE organizes
SET fundraiser_id = s.employee_id
FROM staffmember s
WHERE organizes.fundraiser_id = s.person_id;

-- set the FK
ALTER TABLE organizes
ADD CONSTRAINT fk_organizes_fundraiser_id
FOREIGN KEY (fundraiser_id)
REFERENCES fundraiser(employee_id);

-- add a primary key of fundraiser_id and e_id
ALTER TABLE organizes
ADD CONSTRAINT pk_fundraiser_id_e_id PRIMARY KEY (fundraiser_id, e_id);

--NURSE_ROOM

-- drop FK constraint to nurse_id (which is pointing now to nurse_old)
ALTER TABLE nurse_room
DROP CONSTRAINT nurse_room_nurse_id_fkey;

-- reset the nurse_ids
UPDATE nurse_room
SET nurse_id = s.employee_id
FROM staffmember s
WHERE nurse_room.nurse_id = s.person_id;

-- make employee_id unique for nurse
ALTER TABLE nurse ADD CONSTRAINT nurse_employee_id_unique UNIQUE (employee_id);

-- set the FK of nurse_id to point to nurse employee_id
ALTER TABLE nurse_room
ADD CONSTRAINT fk_nurse_room_nurse_id
FOREIGN KEY (nurse_id)
REFERENCES nurse(employee_id);

-- add d_name (department name) to nurse_room
ALTER TABLE nurse_room
ADD COLUMN d_name VARCHAR NOT NULL DEFAULT 'Maternity Ward';

-- add FK constraint of room_number to room
ALTER TABLE nurse_room
ADD CONSTRAINT fk_nurse_room_room
FOREIGN KEY (room_number, d_name)
REFERENCES room(room_number, d_name);

-- DONATION (donor_id)

-- drop the old FK CONSTRAINTSALTER TABLE donation
ALTER TABLE donation DROP CONSTRAINT donation_donor_id_fkey;

-- add the new FK constraint to point to the new table
ALTER TABLE donation
ADD CONSTRAINT donation_donor_id_fkey
FOREIGN KEY (donor_id)
REFERENCES donor (donor_id)

-- TOWARDS (donor_id)

-- drop current FK
ALTER TABLE towards
DROP CONSTRAINT towards_donor_id_fkey;

-- add a new FK constraint pointing to the new table
ALTER TABLE towards
ADD CONSTRAINT towards_donor_id_fkey
FOREIGN KEY (donor_id)
REFERENCES donor (donor_id);

-- PARTICIPATES_IN (donor_id)

-- drop current FK
ALTER TABLE participates_in
DROP CONSTRAINT participates_in_donor_id_fkey;

-- add a new FK constraint pointing to the new table
ALTER TABLE participates_in
ADD CONSTRAINT participates_in_donor_id_fkey
FOREIGN KEY (donor_id)
REFERENCES donor (donor_id);

-- update mother_ids in baby and then add mother_id fk in baby 
UPDATE baby
SET mother_id = n.patient_id
FROM patient n
WHERE baby.mother_id = n.person_id;

UPDATE prescription
SET patient_id = n.patient_id
FROM patient n
WHERE prescription.patient_id = n.person_id;

-- update fundraiser_id in donor and then add fundraiser_id fk in donor 
UPDATE donor
SET fundraiser_id = n.employee_id
FROM fundraiser n
WHERE donor.fundraiser_id = n.person_id;

ALTER TABLE donor
ADD CONSTRAINT fk_donor_fundraiser_id
FOREIGN KEY (fundraiser_id)
REFERENCES fundraiser (employee_id)

-- drop fk constraint referencing old TABLE
alter table prescription drop constraint prescription_mother_id_fkey;

-- add option that a donation could go to a specific room (add room_number as an optional attribute in towards table)
ALTER TABLE towards
ADD COLUMN room_number INT;

UPDATE towards t
SET room_number = sub.room_number
FROM (
  SELECT DISTINCT ON (r.d_name)
         r.d_name,
         r.room_number
  FROM room r
  JOIN (
    SELECT d_name
    FROM towards
    GROUP BY d_name
  ) td ON td.d_name = r.d_name
  ORDER BY r.d_name, RANDOM()  -- random room per department
) sub
WHERE t.d_name = sub.d_name;

-- add fk of room_number, d_name to towards TABLE
ALTER TABLE towards
ADD CONSTRAINT fk_towards_room_number_d_name
FOREIGN KEY (room_number, d_name)
REFERENCES room (room_number, d_name)





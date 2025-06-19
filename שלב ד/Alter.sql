ALTER TABLE room DROP COLUMN current_occupancy CASCADE;

ALTER TABLE medicine
ADD COLUMN stock INT DEFAULT 100;

ALTER TABLE fundraisingevent
ADD COLUMN e_fundraising_goal INT DEFAULT 20000;


CREATE TABLE maximum_amount_of_patients
(
	type_of_doctor VARCHAR NOT NULL,
	max_patients INT NOT NULL,
	PRIMARY KEY (type_of_doctor)
)
INSERT INTO maximum_amount_of_patients (type_of_doctor, max_patients)
VALUES
    ('doctor', 20),
    ('surgeon', 8),
    ('header doctor', 0),
	('attending', 20),
	('resident', 10),
	('trainee', 5),
	('on-call', 0);

CREATE SEQUENCE IF NOT EXISTS public.donation_donation_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

SELECT MAX(donation_id) FROM donation;
SELECT setval('donation_donation_id_seq', 10000, true);

ALTER TABLE Donation
ALTER COLUMN donation_id SET DEFAULT nextval('donation_donation_id_seq');

CREATE SEQUENCE IF NOT EXISTS public.donor_donor_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

SELECT MAX(donor_id) FROM donor;
SELECT setval('donor_donor_id_seq', 10000, true);

ALTER TABLE Donor
ALTER COLUMN donor_id SET DEFAULT nextval('donor_donor_id_seq');

CREATE SEQUENCE IF NOT EXISTS public.fundraisingevent_e_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

SELECT MAX(e_id) FROM fundraisingevent;
SELECT setval('fundraisingevent_e_id_seq', 10000, true);

ALTER TABLE fundraisingevent
ALTER COLUMN e_id SET DEFAULT nextval('fundraisingevent_e_id_seq');

CREATE SEQUENCE IF NOT EXISTS public.patient_patient_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

SELECT MAX(patient_id) FROM patient;
SELECT setval('patient_patient_id_seq', 10000, true);

ALTER TABLE patient
ALTER COLUMN patient_id SET DEFAULT nextval('patient_patient_id_seq');

CREATE SEQUENCE IF NOT EXISTS public.project_p_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

SELECT MAX(p_id) FROM project;
SELECT setval('project_p_id_seq', 10000, true);

ALTER TABLE project
ALTER COLUMN p_id SET DEFAULT nextval('project_p_id_seq');

alter table mother_old
drop constraint mother_doctor_id_fkey;

drop table baby_id_map;
drop table baby_old;
drop table doctor_old;
drop table donor_id_map_final;
drop table donor_old;
drop table fundraiser_old;
drop table mother_id_map;
drop table mother_old;
drop table nurse_old;
drop table s_id_map;





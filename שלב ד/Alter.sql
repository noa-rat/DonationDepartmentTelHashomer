ALTER TABLE room DROP COLUMN current_occupancy CASCADE;

ALTER TABLE medicine
ADD COLUMN stock INT DEFAULT 100;

ALTER TABLE fundraisingevent
ADD COLUMN e_fundraising_goal INT DEFAULT 20000;
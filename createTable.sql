CREATE TYPE project_status AS ENUM ('ongoing', 'in_preparation', 'closed');

CREATE TYPE donor_type AS ENUM ('individual', 'organization');

CREATE TYPE payment_method AS ENUM ('credit_card', 'standing_order', 'cash', 'check', 'bank_transfer');

CREATE TABLE Department
(
  d_name VARCHAR NOT NULL,
  d_email VARCHAR NOT NULL,
  d_phone VARCHAR NOT NULL,
  d_funds_allocated NUMERIC NOT NULL,
  d_yearly_budget NUMERIC NOT NULL,
  PRIMARY KEY (d_name)
);

CREATE TABLE Project
(
  p_id INT NOT NULL,
  p_name VARCHAR NOT NULL,
  p_description VARCHAR NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  fundraising_goal NUMERIC,
  p_funds_raised NUMERIC,
  status project_status NOT NULL,
  PRIMARY KEY (p_id)
);

CREATE TABLE FundraisingEvent
(
  e_name VARCHAR NOT NULL,
  e_date DATE NOT NULL,
  e_location VARCHAR NOT NULL,
  e_funds_raised NUMERIC,
  PRIMARY KEY (e_name, e_date, e_location)
);

CREATE TABLE StaffMember
(
  s_id INT NOT NULL,
  first_name VARCHAR NOT NULL,
  position VARCHAR NOT NULL,
  s_email VARCHAR NOT NULL,
  s_phone VARCHAR NOT NULL,
  salary NUMERIC NOT NULL,
  last_name VARCHAR NOT NULL,
  PRIMARY KEY (s_id)
);

CREATE TABLE organizes
(
  s_id INT NOT NULL,
  e_name VARCHAR NOT NULL,
  e_date DATE NOT NULL,
  e_location VARCHAR NOT NULL,
  PRIMARY KEY (s_id),
  FOREIGN KEY (s_id) REFERENCES StaffMember(s_id),
  FOREIGN KEY (e_name, e_date, e_location) REFERENCES FundraisingEvent(e_name, e_date, e_location)
);

CREATE TABLE Donor
(
  don_name VARCHAR NOT NULL,
  donor_id INT NOT NULL,
  address VARCHAR NOT NULL,
  is_member BOOL NOT NULL,
  don_email VARCHAR NOT NULL,
  don_phone VARCHAR NOT NULL,
  d_type DONOR_TYPE NOT NULL,
  city VARCHAR NOT NULL,
  country VARCHAR NOT NULL,
  s_id INT,
  PRIMARY KEY (donor_id),
  FOREIGN KEY (s_id) REFERENCES StaffMember(s_id)
);

CREATE TABLE Donation
(
  donation_id INT NOT NULL,
  d_date DATE NOT NULL,
  d_amount NUMERIC NOT NULL,
  d_method PAYMENT_METHOD NOT NULL,
  donor_id INT NOT NULL,
  p_id INT,
  PRIMARY KEY (donation_id, donor_id),
  FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
  FOREIGN KEY (p_id) REFERENCES Project(p_id)
);

CREATE TABLE towards
(
  donation_id INT NOT NULL,
  donor_id INT NOT NULL,
  d_name VARCHAR NOT NULL,
  PRIMARY KEY (donation_id, donor_id, d_name),
  FOREIGN KEY (donation_id, donor_id) REFERENCES Donation(donation_id, donor_id),
  FOREIGN KEY (d_name) REFERENCES Department(d_name)
);

CREATE TABLE participates_in
(
  donor_id INT NOT NULL,
  e_name VARCHAR NOT NULL,
  e_date DATE NOT NULL,
  e_location VARCHAR NOT NULL,
  PRIMARY KEY (donor_id, e_name, e_date, e_location),
  FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
  FOREIGN KEY (e_name, e_date, e_location) REFERENCES FundraisingEvent(e_name, e_date, e_location)
);

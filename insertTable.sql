-- Insert data into Department
INSERT INTO Department (d_name, d_email, d_phone, d_funds_allocated, d_yearly_budget) 
VALUES ('Cardiology Hopkins Center', 'cardioh@hospital.org', 123456789, 50000, 200000),
       ('Oncology Hopkins Center', 'oncologyh@hospital.org', 987654321, 70000, 250000),
       ('Pediatrics Hopkins Center', 'pediatricsh@hospital.org', 111222333, 60000, 220000);

-- Insert data into Project
INSERT INTO Project (p_id, p_name, p_description, start_date, end_date, fundraising_goal, p_funds_raised, status) 
VALUES (1412, 'Cancer Research Hopkins Initiative', 'Research on new treatments', '2024-01-01', '2025-12-31', 1000000, 250000, 'ongoing'),
       (1413, 'Rehabilitation Center Expansion Hopkins Initiative', 'New pediatric wing', '2024-03-15', NULL, 2000000, 500000, 'in_preparation'),
       (1414, 'Heart Disease Awareness Hopkins Initiative', 'Public awareness campaign', '2024-06-01', '2024-12-01', 50000, 10000, 'ongoing');

-- Insert data into FundraisingEvent
INSERT INTO FundraisingEvent (e_name, e_date, e_location, e_funds_raised) 
VALUES ('Annual Charity Gala at the Riviera', '2024-05-20', 'Grand Hotel', 100000),
       ('Marathon for Hope Live On', '2024-06-15', 'City Park', 50000),
       ('Art for Disabilities Auction', '2024-07-10', 'Downtown Gallery', 75000);

-- Insert data into StaffMember
INSERT INTO StaffMember (s_id, first_name, last_name, "position", s_email, s_phone, salary) 
VALUES (1412, 'John', 'Doe', 'Director', 'johndoe@hospital.org', 123123123, 90000),
       (1413, 'Jane', 'Smith', 'Fundraising Coordinator', 'janesmith@hospital.org', 321321321, 75000),
       (1414, 'Emily', 'Brown', 'Project Manager', 'emilybrown@hospital.org', 555666777, 85000);

-- Insert data into organizes
INSERT INTO organizes (s_id, e_name, e_date, e_location) 
VALUES (1414, 'Annual Charity Gala at the Riviera', '2024-05-20', 'Grand Hotel'),
       (1414, 'Marathon for Hope Live On', '2024-06-15', 'City Park'),
       (1412, 'Art for Disabilities Auction', '2024-07-10', 'Downtown Gallery');

-- Insert data into Donor
INSERT INTO Donor (donor_id, don_name, address, is_member, don_email, don_phone, d_type, city, country, s_id) 
VALUES (505, 'Alice Green', '123 Main St', TRUE, 'alicegreen@email.com', 999888777, 'individual', 'New York', 'USA', 1412),
       (506, 'Global Aid Inc.', '456 Elm St', FALSE, 'contact@globalaid.org', 888777666, 'organization', 'London', 'UK', 1412),
       (507, 'Bob White', '789 Oak St', TRUE, 'bobwhite@email.com', 777666555, 'individual', 'Paris', 'France', 1412);

-- Insert data into Donation
INSERT INTO Donation (donation_id, d_date, d_amount, d_method, donor_id, p_id) 
VALUES (666, '2024-05-21', 10000, 'credit_card', 505, 1),
       (667, '2024-06-16', 5000, 'bank_transfer', 506, 2),
       (668, '2024-07-11', 7500, 'cash', 507, 3);

-- Insert data into towards
INSERT INTO towards (donation_id, donor_id, d_name) 
VALUES (666, 505, 'Cardiology Hopkins Center'),
       (667, 506, 'Oncology Hopkins Center'),
       (668, 507, 'Pediatrics Hopkins Center');

-- Insert data into participates_in
INSERT INTO participates_in (donor_id, e_name, e_date, e_location) 
VALUES (101, 'Annual Charity Gala at the Riviera', '2024-05-20', 'Grand Hotel'),
       (102, 'Marathon for Hope Live On', '2024-06-15', 'City Park'),
       (103, 'Art for Disabilities Auction', '2024-07-10', 'Downtown Gallery');

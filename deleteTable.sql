-- Drop tables in reverse order to avoid foreign key constraints
DROP TABLE IF EXISTS participates_in CASCADE;
DROP TABLE IF EXISTS towards CASCADE;
DROP TABLE IF EXISTS Donation CASCADE;
DROP TABLE IF EXISTS Donor CASCADE;
DROP TABLE IF EXISTS organizes CASCADE;
DROP TABLE IF EXISTS StaffMember CASCADE;
DROP TABLE IF EXISTS FundraisingEvent CASCADE;
DROP TABLE IF EXISTS Project CASCADE;
DROP TABLE IF EXISTS Department CASCADE;

-- Drop types after tables to avoid dependency issues
DROP TYPE IF EXISTS donor_type CASCADE;
DROP TYPE IF EXISTS payment_method CASCADE;
DROP TYPE IF EXISTS project_status CASCADE;

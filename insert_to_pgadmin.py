from sqlalchemy import create_engine, Column, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

# Define the base class for SQLAlchemy models
Base = declarative_base()


# Define the Department table model
class Department(Base):
    __tablename__ = 'Department'

    d_name = Column(String, primary_key=True, nullable=False)
    d_email = Column(String, nullable=False)
    d_phone = Column(String, nullable=False)  # Ensure d_phone is a VARCHAR (String)
    d_funds_allocated = Column(Numeric, nullable=False)
    d_yearly_budget = Column(Numeric, nullable=False)


# List of possible research department names
research_departments = [
    "Cancer Technological Research", "Neuroscience Technological Research", "Cardiology Technological Research",
    "Genetics Technological Research",
    "Immunology Technological Research", "Microbiology Technological Research", "Virology Technological Research",
    "Pharmacology Technological Research",
    "Pediatric Technological Research", "Endocrinology Technological Research", "Orthopedic Technological Research",
    "Radiology Technological Research"
]

# Initialize Faker to generate fake data
fake = Faker()

# Create a connection to the database
DATABASE_URL = "postgresql://adina:almond890@localhost:5432/TelHashomerDonationsDepartment"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


# Function to generate a random department row
def generate_department_row():
    d_name = random.choice(research_departments)
    d_email = f"{d_name.replace(' ', '').lower()}@hospital.com"
    d_phone = fake.phone_number()  # Faker generates phone numbers as strings
    d_funds_allocated = round(random.uniform(500000, 5000000), 2)  # Allocated funds between 500k and 5 million
    d_yearly_budget = round(random.uniform(200000, 1000000), 2)  # Yearly budget between 200k and 1 million

    return Department(
        d_name=d_name,
        d_email=d_email,
        d_phone=d_phone,
        d_funds_allocated=d_funds_allocated,
        d_yearly_budget=d_yearly_budget
    )


# Function to insert multiple department rows
def insert_departments(num_rows=10):
    departments = [generate_department_row() for _ in range(num_rows)]

    try:
        for dept in departments:
            # Check if the department already exists based on the department name
            existing_dept = session.query(Department).filter_by(d_name=dept.d_name).first()
            if existing_dept:
                print(f"Skipping {dept.d_name}, it already exists.")
            else:
                session.add(dept)  # Add department only if it doesn't exist

        session.commit()  # Commit the transaction only if all records are successfully inserted
        print(f"{num_rows} department rows inserted successfully.")

    except Exception as e:
        session.rollback()  # Rollback in case of any failure
        print(f"Error: {e}")
    finally:
        session.close()  # Always close the session to release resources


# Run the script to insert 10 department rows
if __name__ == "__main__":
    insert_departments(10)  # Adjust the number of rows as needed

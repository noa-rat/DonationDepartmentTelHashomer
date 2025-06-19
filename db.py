import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="IntegratedDonationsMaternity",
            user="adina",
            password="almond890",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Database connection failed:", e)
        return None
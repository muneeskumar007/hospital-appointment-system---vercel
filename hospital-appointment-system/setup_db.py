import psycopg2
import os

# Connect to PostgreSQL
database_url = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/hospital_db')
conn = psycopg2.connect(database_url)
cursor = conn.cursor()

# Create tables if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'patient',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    experience INTEGER NOT NULL,
    fee DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES users(id),
    doctor_id INTEGER NOT NULL REFERENCES doctors(id),
    slot_id INTEGER,
    token INTEGER,
    status VARCHAR(20) DEFAULT 'Booked',
    appointment_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert sample doctors (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM doctors")
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute("""
    INSERT INTO doctors (name, specialty, experience, fee) VALUES
    ('Dr. John Smith', 'Cardiology', 10, 500.00),
    ('Dr. Sarah Johnson', 'Dermatology', 8, 400.00),
    ('Dr. Michael Brown', 'Orthopedics', 12, 600.00)
    """)

conn.commit()
cursor.close()
conn.close()

print("Database schema created/updated successfully!")
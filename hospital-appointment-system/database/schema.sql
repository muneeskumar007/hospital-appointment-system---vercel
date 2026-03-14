
-- (Optional) Create database when running locally; Vercel provides DATABASE_URL in production.
-- CREATE DATABASE hospital_db;
-- \c hospital_db

CREATE TABLE IF NOT EXISTS doctors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    experience INTEGER NOT NULL,
    fee NUMERIC(10,2) NOT NULL
);




CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'patient' NOT NULL
);

CREATE TABLE IF NOT EXISTS slots (
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER NOT NULL REFERENCES doctors(id),
    slot_time VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES users(id),
    doctor_id INTEGER NOT NULL REFERENCES doctors(id),
    slot_id INTEGER REFERENCES slots(id),
    token INTEGER,
    status VARCHAR(20) DEFAULT 'Booked'
);




INSERT INTO doctors (name, specialty, experience, fee)
VALUES
('Dr. Anjali', 'Pediatrician', 8, 450.00),
('Dr. Suresh', 'Neurologist', 15, 700.00),
('Dr. Priya', 'Gynecologist', 9, 500.00),
('Dr. Ramesh', 'ENT Specialist', 11, 550.00),
('Dr. Kumar', 'Cardiologist', 10, 500.00),
('Dr. Meena', 'Dermatologist', 7, 400.00),
('Dr. Raj', 'Orthopedic', 12, 600.00);
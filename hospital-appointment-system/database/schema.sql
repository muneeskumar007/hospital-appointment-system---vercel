


CREATE DATABASE hospital_db;
USE hospital_db;



CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialty VARCHAR(100),
    experience INT,
    fee INT
);





CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
password VARCHAR(100),
role VARCHAR(20)
);

CREATE TABLE slots(
id INT AUTO_INCREMENT PRIMARY KEY,
doctor_id INT,
slot_time VARCHAR(50)
);

CREATE TABLE appointments(
id INT AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
doctor_id INT,
slot_id INT,
token INT,
status VARCHAR(20)
);




('Dr. Kumar','Cardiologist',10,500),
('Dr. Meena','Dermatologist',7,400),
('Dr. Raj','Orthopedic',12,600);





INSERT INTO doctors (name, specialty, experience, fee)
VALUES
('Dr. Anjali', 'Pediatrician', 8, 450),
('Dr. Suresh', 'Neurologist', 15, 700),
('Dr. Priya', 'Gynecologist', 9, 500),
('Dr. Ramesh', 'ENT Specialist', 11, 550);
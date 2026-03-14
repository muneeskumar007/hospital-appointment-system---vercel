from app.services.db import db
from datetime import datetime, date

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    slot_id = db.Column(db.Integer)
    token = db.Column(db.Integer)
    status = db.Column(db.String(20), default='Booked')
    appointment_date = db.Column(db.Date, default=date.today)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    patient = db.relationship('User', backref='appointments')
    doctor = db.relationship('Doctor', backref='appointments')
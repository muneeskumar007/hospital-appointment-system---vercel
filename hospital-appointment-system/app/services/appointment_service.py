from app.services.db import db
from app.models.appointment_model import Appointment

def book_appointment(patient_id, doctor_id, slot_id=None):
    appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, slot_id=slot_id)
    db.session.add(appointment)
    db.session.commit()
    return appointment

def get_patient_appointments(patient_id):
    return Appointment.query.filter_by(patient_id=patient_id).all()

def cancel_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return True
    return False
    )

    db.commit()
    db.close()

from flask import Blueprint, render_template, session
from app.models.appointment_model import Appointment

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    appointments = Appointment.query.filter_by(patient_id=session["user_id"]).all()
    return render_template("dashboard.html", appointments=appointments)
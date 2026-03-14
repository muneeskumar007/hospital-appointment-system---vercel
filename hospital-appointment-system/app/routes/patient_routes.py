from flask import Blueprint, render_template, session, redirect, url_for
from app.models.doctor_model import Doctor

patient_bp = Blueprint("patient", __name__)

@patient_bp.route("/patient/dashboard")
def patient_dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    doctors = Doctor.query.all()
    return render_template("patient_dashboard.html", doctors=doctors)
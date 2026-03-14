from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from app.models.doctor_model import Doctor
from app.services.appointment_service import book_appointment

appointment_bp = Blueprint("appointment", __name__)


@appointment_bp.route("/book/<int:doctor_id>", methods=["GET", "POST"])
def book_appointment_route(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if not doctor:
        return "Doctor not found"

    if request.method == "POST":
        if "user_id" not in session:
            flash("Please login to book an appointment", "error")
            return redirect(url_for("auth.login"))

        # Assuming slot_id is passed or default to None
        slot_id = request.form.get("slot_id")
        appointment = book_appointment(session["user_id"], doctor_id, slot_id)
        flash("Appointment booked successfully!", "success")
        return redirect(url_for("appointment.my_appointments"))

    return render_template("appointment.html", doctor=doctor)


@appointment_bp.route("/my-appointments")
def my_appointments():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    from app.services.appointment_service import get_patient_appointments
    appointments = get_patient_appointments(session["user_id"])
    return render_template("patient_dashboard.html", appointments=appointments)
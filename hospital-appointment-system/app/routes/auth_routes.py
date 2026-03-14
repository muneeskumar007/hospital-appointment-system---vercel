from flask import Blueprint, render_template, request, redirect, flash, session, url_for

from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import create_user, get_user_by_email
import re
from functools import wraps

auth_bp = Blueprint("auth", __name__)
@auth_bp.route("/login", methods=["GET","POST"])
def login():

    error = None

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = get_user_by_email(email)

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id
            session["user_name"] = user.name

            next_page = request.args.get("next")

            if next_page:
                return redirect(next_page)

            return redirect("/doctors")

        else:
            error = "Invalid email or password"

    return render_template("login.html", error=error)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        role = request.form.get("role", "patient").strip()

        # Simple validation
        if not name or not email or not password:
            flash("All fields are required!", "error")
            return redirect("/register")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email address!", "error")
            return redirect("/register")
        if len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
            return redirect("/register")

        # Hash password safely
        # hashed_password = generate_password_hash(password, method="sha256")
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)

        try:
            # Check if email already exists
            existing_user = get_user_by_email(email)
            if existing_user:
                flash("Email already registered.", "error")
                return redirect("/register")

            # Save user
            create_user(name, email, hashed_password, role)
            flash("Registration successful! Please login.", "success")
            return redirect("/login")

        except Exception as e:
            print("Registration Error:", e)
            flash("Registration failed due to server error.", "error")
            return redirect("/register")

    # GET request
    return render_template("register.html")



@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function
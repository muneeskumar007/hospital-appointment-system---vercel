from flask import Flask
from app.services.db import mysql

def create_app():

    app = Flask(__name__)

    # DATABASE CONFIG
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "root123"
    app.config["MYSQL_DB"] = "hospital_db"

    mysql.init_app(app)

    # IMPORT ROUTES
    from app.routes.doctor_routes import doctor_bp
    from app.routes.auth_routes import auth_bp

    # REGISTER BLUEPRINTS
    app.register_blueprint(doctor_bp)
    app.register_blueprint(auth_bp)

    return app
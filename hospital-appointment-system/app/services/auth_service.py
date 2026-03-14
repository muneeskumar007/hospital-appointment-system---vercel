from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import create_user, get_user_by_email

def register_user(name,email,password,role):

    hashed_password = generate_password_hash(password)

    create_user(name,email,hashed_password,role)


def login_user(email,password):

    user = get_user_by_email(email)

    if user and check_password_hash(user.password,password):
        return user

    return None
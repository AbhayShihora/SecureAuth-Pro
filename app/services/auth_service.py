from app.models.user import User
from app.extensions import db, bcrypt
from flask_login import login_user
from app.utils.otp import generate_otp
from datetime import datetime, timedelta
from app.services.mail_service import send_otp_email

#Registration service function
def register_user(form):
    try:

        existing_user = User.query.filter_by(
            username=form.username.data
        ).first()

        if existing_user:
            return False, "Username already exists."

        existing_email = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_email:
            return False, "Email already exists."

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        otp = generate_otp()
        expiry = datetime.utcnow() + timedelta(minutes=5)

        user = User(
                    full_name=form.full_name.data, username=form.username.data,
                    email=form.email.data,  password_hash=hashed_password,
                    is_verified=False, otp=otp,otp_expiry=expiry
                )

        #Send OTP email
        send_otp_email(user.email, otp)


        db.session.add(user)

        db.session.commit()
        return True, "Registration successful!"

    except Exception as e:
        db.session.rollback()
        return False, str(e)

#Login service function
def login_user_service(form):
    """
    Authenticate a user using email and password.
    Returns:
        (True, "Login successful.") on success
        (False, "Error message") on failure
    """

    # Step 1: Find user by email
    user = User.query.filter_by(email=form.email.data).first()

    # Step 2: User not found
    if not user:
        return False, "No account found with this email."

    if not user.is_active:
        return False, "Your account has been deactivated. Please contact the administrator."
    
    if not user.is_verified:
        return False, "Please verify your email before logging in."

    # Step 3: Verify password
    if not bcrypt.check_password_hash(
        user.password_hash,
        form.password.data
    ):
        return False, "Incorrect password."

    # Step 4: Login user
    login_user(user, remember=form.remember.data)

    return True, "Login successful."

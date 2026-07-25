from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import logout_user, login_required

from app.forms.auth_forms import RegistrationForm, LoginForm, OTPForm
from app.services.auth_service import register_user, login_user_service
from app.models.user import User
from app.extensions import db
from datetime import datetime, timedelta 

from app.utils.otp import generate_otp

#For sending test email
from app.services.mail_service import send_otp_email


# Create Blueprint
auth = Blueprint("auth", __name__)

# -------------------------
# Registration Route
# -------------------------
@auth.route("/register", methods=["GET", "POST"])
def register():
    print("===== REGISTER ROUTE CALLED =====")
    print("Method:", request.method)

    form = RegistrationForm()

    if form.validate_on_submit():
        print("VALIDATION PASSED")

        success, message = register_user(form)

        if success:
            session["verification_email"] = form.email.data

            flash(
                "Registration successful! Please verify your email using the OTP.",
                "success"
            )

            return redirect(url_for("auth.verify_otp"))
        else:
            flash(message, "danger")

    else:
        print("VALIDATION FAILED")
        print(form.errors)

    return render_template("auth/register.html", form=form)


# -------------------------
# Login Route
# -------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        success, message = login_user_service(form)

        if success:
            flash(message, "success")
            return redirect(url_for("main.dashboard"))

        flash(message, "danger")

    return render_template("auth/login.html", form=form)


# -------------------------
# Logout Route
# -------------------------
@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("You have been logged out successfully.", "success")

    return redirect(url_for("auth.login"))

#Verify OTP Route
@auth.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():

    email = session.get("verification_email")

    if not email:
        flash("Verification session expired. Please register again.", "warning")
        return redirect(url_for("auth.register"))

    form = OTPForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("User not found.", "danger")
            return redirect(url_for("auth.register"))

        if user.otp != form.otp.data:
            flash("Invalid OTP.", "danger")
            return render_template("auth/verify_otp.html", form=form)

        if datetime.utcnow() > user.otp_expiry:
            flash("OTP has expired.", "danger")
            return render_template("auth/verify_otp.html", form=form)

        user.is_verified = True
        user.otp = None
        user.otp_expiry = None

        db.session.commit()

        session.pop("verification_email", None)

        flash("Email verified successfully! Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/verify_otp.html", form=form)

#resend OTP Route
@auth.route("/resend-otp")
def resend_otp():

    email = session.get("verification_email")

    if not email:
        flash("Session expired. Please register again.", "warning")
        return redirect(url_for("auth.register"))

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("auth.register"))

    otp = generate_otp()

    user.otp = otp
    user.otp_expiry = datetime.utcnow() + timedelta(minutes=5)

    db.session.commit()

    send_otp_email(user.email, otp)

    flash("A new OTP has been sent to your email.", "success")

    return redirect(url_for("auth.verify_otp"))
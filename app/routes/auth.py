from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import logout_user, login_required

from app.forms.auth_forms import RegistrationForm, LoginForm, OTPForm, ForgotPasswordForm, ResetPasswordForm
from app.services.auth_service import register_user, login_user_service
from app.models.user import User
from app.extensions import db, bcrypt
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

#Forgot Password Route
@auth.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    form = ForgotPasswordForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash("No account found with this email.", "danger")
            return render_template("auth/forgot_password.html", form=form)

        otp = generate_otp()

        user.otp = otp
        user.otp_expiry = datetime.utcnow() + timedelta(minutes=5)

        db.session.commit()

        send_otp_email(user.email, otp)

        session["reset_email"] = user.email

        flash("OTP sent to your email.", "success")

        return redirect(url_for("auth.verify_reset_otp"))

    return render_template("auth/forgot_password.html", form=form)

#Reset Password Route
@auth.route("/verify-reset-otp", methods=["GET", "POST"])
def verify_reset_otp():

    email = session.get("reset_email")

    if not email:
        flash("Session expired.", "warning")
        return redirect(url_for("auth.forgot_password"))

    form = OTPForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("User not found.", "danger")
            return redirect(url_for("auth.forgot_password"))

        if user.otp != form.otp.data:
            flash("Invalid OTP.", "danger")
            return render_template("auth/verify_reset_otp.html", form=form)

        if datetime.utcnow() > user.otp_expiry:
            flash("OTP has expired.", "danger")
            return render_template("auth/verify_reset_otp.html", form=form)

        session["password_reset_verified"] = True

        return redirect(url_for("auth.reset_password"))

    return render_template("auth/verify_reset_otp.html", form=form)

#Reset Password Route
@auth.route("/reset-password", methods=["GET", "POST"])
def reset_password():

    # Check if OTP verification was completed
    if not session.get("password_reset_verified"):
        flash("Please verify your OTP first.", "warning")
        return redirect(url_for("auth.forgot_password"))

    email = session.get("reset_email")

    if not email:
        flash("Session expired.", "warning")
        return redirect(url_for("auth.forgot_password"))

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("auth.forgot_password"))

    form = ResetPasswordForm()

    if form.validate_on_submit():

        # Hash the new password
        user.password_hash = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        # Clear OTP information
        user.otp = None
        user.otp_expiry = None

        db.session.commit()

        # Remove session values
        session.pop("reset_email", None)
        session.pop("password_reset_verified", None)

        flash(
            "Password reset successful! Please login.",
            "success"
        )

        return redirect(url_for("auth.login"))

    return render_template(
        "auth/reset_password.html",
        form=form
    )
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import logout_user, login_required

from app.forms.auth_forms import RegistrationForm, LoginForm
from app.services.auth_service import register_user, login_user_service

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
            flash(message, "success")
            return redirect(url_for("auth.login"))
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
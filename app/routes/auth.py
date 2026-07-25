from app.forms.auth_forms import RegistrationForm
from app.services.auth_service import register_user
from flask import Blueprint, render_template, redirect, url_for, flash, request

auth = Blueprint("auth", __name__)

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

@auth.route("/login")
def login():
    return "Login Page Coming Soon..."


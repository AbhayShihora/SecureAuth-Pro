from app.forms.auth_forms import RegistrationForm, LoginForm
from app.services.auth_service import register_user, login_user_service
from flask import Blueprint, render_template, redirect, url_for, flash, request

auth = Blueprint("auth", __name__)

#Registration route
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

#Login route
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


from flask import Blueprint, render_template

from app.forms.auth_forms import RegistrationForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    return render_template(
        "auth/register.html",
        form=form
    )
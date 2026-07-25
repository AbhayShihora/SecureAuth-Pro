from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint("main", __name__)

#Home route
@main.route("/")
def home():
    return render_template("index.html")

#Dashboard route
@main.route("/dashboard")
@login_required
def dashboard():
    return "<h1>Welcome to Dashboard 🚀</h1>"
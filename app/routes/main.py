from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.utils.decorators import admin_required
from app.models.user import User
from app.extensions import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

#dashboard route for logged-in users
@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

#Admin-only route
@main.route("/admin")
@login_required
@admin_required
def admin_dashboard():
    return render_template("admin/dashboard.html")


#Admin route to manage users
@main.route("/admin/users")
@login_required
@admin_required
def manage_users():

    users = User.query.order_by(User.id).all()

    return render_template(
        "admin/manage_users.html",
        users=users
    )

#Admin route to toggle user status (active/inactive)
@main.route("/admin/toggle-user/<int:user_id>")
@login_required
@admin_required
def toggle_user_status(user_id):

    user = User.query.get_or_404(user_id)

    # Prevent admin from disabling themselves
    if user.id == current_user.id:
        flash("You cannot deactivate your own account.", "warning")
        return redirect(url_for("main.manage_users"))

    user.is_active = not user.is_active

    db.session.commit()

    flash("User status updated successfully.", "success")

    return redirect(url_for("main.manage_users"))

#Admin route to change user role (user/admin)
@main.route("/admin/change-role/<int:user_id>")
@login_required
@admin_required
def change_role(user_id):
    user = User.query.get_or_404(user_id)

    # Prevent changing your own role
    if user.id == current_user.id:
        flash("You cannot change your own role.", "warning")
        return redirect(url_for("main.manage_users"))

    if user.role == "user":
        user.role = "admin"
    else:
        user.role = "user"

    db.session.commit()
    flash("User role updated successfully.", "success")

    return redirect(url_for("main.manage_users"))
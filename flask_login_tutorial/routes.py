"""Logged-in page routes."""

from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user

from .models import db

# Blueprint Configuration
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates", static_folder="static")


@main_blueprint.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    current_user.last_login = db.func.now()
    db.session.commit()
    return render_template(
        "dashboard.jinja2",
        title="Flask-Login Tutorial",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@main_blueprint.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_blueprint.login"))

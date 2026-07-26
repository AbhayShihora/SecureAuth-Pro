from flask import Flask, app

from config import Config
from app.extensions import (
    db,
    login_manager,
    bcrypt,
    mail,
    migrate,
)

from app.routes.main import main
from app.routes.auth import auth
from app.models import User

from flask_migrate import upgrade


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Extensions
    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

# ================= Mail Debug =================
    print("=" * 60)
    print("MAIL_SERVER        :", app.config["MAIL_SERVER"])
    print("MAIL_PORT          :", app.config["MAIL_PORT"])
    print("MAIL_USE_TLS       :", app.config["MAIL_USE_TLS"])
    print("MAIL_USE_SSL       :", app.config["MAIL_USE_SSL"])
    print("MAIL_USERNAME      :", app.config["MAIL_USERNAME"])
    print("MAIL_DEFAULT_SENDER:", app.config["MAIL_DEFAULT_SENDER"])
    print("=" * 60)
# =============================================
    # Flask-Login Configuration
    login_manager.login_message_category = "warning"

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
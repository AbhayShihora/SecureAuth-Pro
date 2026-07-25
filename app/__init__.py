from flask import Flask

from config import Config
from app.extensions import (
    db,
    login_manager,
    bcrypt,
    mail,
    migrate,
)

# Import Blueprints
from app.routes.main import main
from app.routes.auth import auth

# Import Models
from app.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Flask-Login Configuration
    # We'll enable login_view after creating the login route
    # login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
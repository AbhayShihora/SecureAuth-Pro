from flask import Flask
from app.routes.main import main

from config import Config
from app.extensions import (
    db,
    login_manager,
    bcrypt,
    mail,
    migrate,
)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    #for main.py page
    app.register_blueprint(main)
    return app
from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "<h1>🚀 SecureAuth Pro is Running Successfully!</h1>"
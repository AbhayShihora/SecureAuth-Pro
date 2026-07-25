from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

with app.app_context():
    user = User.query.filter_by(email="shihoraabhay@gmail.com").first()

    if user:
        user.role = "admin"
        db.session.commit()
        print("User promoted to admin.")
    else:
        print("User not found.")
from flask_login import UserMixin

from app.extensions import db
from app.models.base import BaseModel

from datetime import datetime

class User(UserMixin, BaseModel):
    __tablename__ = "users"

    username = db.Column(db.String(30),unique=True,nullable=False)

    full_name = db.Column(db.String(100),nullable=False)

    email = db.Column(db.String(120), unique=True,nullable=False )

    password_hash = db.Column(db.String(255),nullable=False)

    profile_image = db.Column(db.String(255),default="default.png")

    is_verified = db.Column(db.Boolean,default=False)

    is_active = db.Column(db.Boolean, default=True)

    last_login = db.Column(db.DateTime,  nullable=True )
    
    otp = db.Column(db.String(6), nullable=True)

    otp_expiry = db.Column(db.DateTime, nullable=True)

    role = db.Column(db.String(20), nullable=False,default="admin")

    def __repr__(self):
        return f"<User {self.username}>"
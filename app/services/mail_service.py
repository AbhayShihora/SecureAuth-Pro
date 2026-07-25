from flask import current_app
from flask_mail import Message
from app.extensions import mail


def send_otp_email(recipient_email, otp):
    print("MAIL_SERVER:", current_app.config["MAIL_SERVER"])
    print("MAIL_PORT:", current_app.config["MAIL_PORT"])
    print("MAIL_USE_TLS:", current_app.config["MAIL_USE_TLS"])
    print("Sending email...")
    mail.send(msg)
    print("Email sent!")
    """msg = Message(
        subject="SecureAuth Pro - Email Verification",
        sender=current_app.config["MAIL_DEFAULT_SENDER"],
        recipients=[recipient_email]
    )

    msg.body = f"""
"""Hello,

Thank you for registering with SecureAuth Pro.

Your One-Time Password (OTP) is:

========================
        {otp}
========================

This OTP is valid for 5 minutes.

If you did not register, please ignore this email.

Regards,
SecureAuth Pro Team
"""

    mail.send(msg)

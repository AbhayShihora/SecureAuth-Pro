from flask_mail import Message
from app.extensions import mail

def send_otp_email(email, otp):
    print(f"Sending OTP to: {email}")

    msg = Message(
        subject="SecureAuth Pro - OTP Verification",
        recipients=[email]
    )

    msg.body = f"Your OTP is: {otp}"

    try:
        print("Connecting...")
        mail.send(msg)
        print("✅ Email accepted by SMTP server")
    except Exception as e:
        print("❌ SMTP ERROR:", repr(e))
        raise
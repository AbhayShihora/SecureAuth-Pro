from flask_mail import Message
from app.extensions import mail


def send_otp_email(email, otp):
    print(f"Sending OTP to: {email}")

    msg = Message(
        subject="OTP Verification",
        recipients=[email]
    )

    msg.html = f"""
    <h2>Email Verification</h2>

    <p>Hello,</p>

    <p>Your OTP for email verification is:</p>

    <h1 style="color:#2563eb;">{otp}</h1>

    <p>This OTP will expire in <strong>10 minutes</strong>.</p>

    <p>If you didn't request this OTP, you can safely ignore this email.</p>

    <br>

    <p>Regards,<br>
    <strong>SecureAuth Pro Team</strong></p>
    """

    mail.send(msg)

    print("✅ OTP email sent successfully.")
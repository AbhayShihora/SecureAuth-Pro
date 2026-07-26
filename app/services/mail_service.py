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
    <h1>{otp}</h1>
    """

    try:
        try:
            print("Connecting to SMTP server...")
            mail.send(msg)
            print("✅ OTP email sent successfully.")
        except Exception as e:
            print("❌ MAIL ERROR:", repr(e))
            raise
        print("✅ OTP email sent successfully.")
    except Exception as e:
        print("❌ MAIL ERROR:", e)
        raise
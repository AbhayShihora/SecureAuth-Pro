import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")


def send_otp_email(email, otp):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [email],
        "subject": "OTP Verification",
        "html": f"""
        <h2>Email Verification</h2>

        <p>Your OTP is:</p>

        <h1>{otp}</h1>

        <p>This OTP expires in 10 minutes.</p>
        """
    })
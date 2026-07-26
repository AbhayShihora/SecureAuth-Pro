import os
import requests

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


def send_otp_email(email, otp):
    api_key = os.getenv("BREVO_API_KEY")

    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json",
    }

    payload = {
        "sender": {
            "name": "SecureAuth Pro",
            "email": os.getenv("MAIL_DEFAULT_SENDER"),
        },
        "to": [
            {
                "email": email
            }
        ],
        "subject": "OTP Verification - SecureAuth Pro",
        "htmlContent": f"""
        <h2>SecureAuth Pro</h2>

        <p>Your OTP is:</p>

        <h1 style="color:#0d6efd;">{otp}</h1>

        <p>This OTP is valid for 10 minutes.</p>

        <p>If you didn't request this OTP, please ignore this email.</p>
        """
    }

    response = requests.post(
        BREVO_API_URL,
        headers=headers,
        json=payload,
        timeout=15,
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()
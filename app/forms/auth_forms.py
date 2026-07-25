from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField,SubmitField,)
from wtforms.validators import (DataRequired,Length,Email,EqualTo,)

# Registration form class
class RegistrationForm(FlaskForm):
    full_name = StringField("Full Name",validators=[DataRequired(), Length(min=3, max=100)  ] )

    username = StringField( "Username",validators=[ DataRequired(),Length(min=4, max=30) ])

    email = StringField("Email", validators=[ DataRequired(),Email(),  Length(max=120)    ] )

    password = PasswordField("Password",validators=[DataRequired(),Length(min=8)] )

    confirm_password = PasswordField( "Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords must match.") ])

    accept_terms = BooleanField( "I accept the Terms & Conditions", validators=[DataRequired()])

    submit = SubmitField("Create Account")

#Login form class
class LoginForm(FlaskForm):
    email = StringField("Email",validators=[ DataRequired(),Email()])

    password = PasswordField(validators=[DataRequired()])

    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")

#OTP form class
class OTPForm(FlaskForm):
    otp = StringField(
        "Enter OTP",
        validators=[
            DataRequired(),
            Length(min=6, max=6)
        ]
    )

    submit = SubmitField("Verify OTP")

#Forgot Password form class
class ForgotPasswordForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField("Send OTP")

#Reset Password form class
class ResetPasswordForm(FlaskForm):

    password = PasswordField(
        "New Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password")
        ]
    )

    submit = SubmitField("Reset Password")
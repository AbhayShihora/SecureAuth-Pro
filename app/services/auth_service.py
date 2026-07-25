from app.models.user import User
from app.extensions import db, bcrypt
from flask_login import login_user

#Registration service function
def register_user(form):
    print("INSIDE register_user()")
    try:
        print("Step 1: Checking username")

        existing_user = User.query.filter_by(
            username=form.username.data
        ).first()

        if existing_user:
            return False, "Username already exists."

        print("Step 2: Checking email")

        existing_email = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_email:
            return False, "Email already exists."

        print("Step 3: Hashing password")

        print("Password:", repr(form.password.data))
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        print("Step 4: Creating user")

        user = User(
            full_name=form.full_name.data,
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password
        )

        print("Step 5: Adding to session")

        db.session.add(user)

        print("Step 6: Commit")

        db.session.commit()

        print("✅ User Saved Successfully")

        return True, "Registration successful!"

    except Exception as e:
        db.session.rollback()
        print("❌ ERROR:", e)
        return False, str(e)

#Login service function
def login_user_service(form):
    """
    Authenticate a user using email and password.
    Returns:
        (True, "Login successful.") on success
        (False, "Error message") on failure
    """

    # Step 1: Find user by email
    user = User.query.filter_by(email=form.email.data).first()

    # Step 2: User not found
    if not user:
        return False, "No account found with this email."

    # Step 3: Verify password
    if not bcrypt.check_password_hash(
        user.password_hash,
        form.password.data
    ):
        return False, "Incorrect password."

    # Step 4: Login user
    login_user(user, remember=form.remember.data)

    return True, "Login successful."
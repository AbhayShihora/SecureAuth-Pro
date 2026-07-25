# 🔐 SecureAuth Pro

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

![GitHub Repo stars](https://img.shields.io/github/stars/AbhayShihora/SecureAuth-Pro?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/AbhayShihora/SecureAuth-Pro?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/AbhayShihora/SecureAuth-Pro?style=for-the-badge)

</p>

<p align="center">
    A Secure Authentication & User Management System built with Flask following modern backend development practices.
</p>

---

# 🌐 Live Demo

🚀 **Live Application**

👉 **YOUR_RENDER_LINK**


---

# 📌 Project Overview

SecureAuth Pro is a secure authentication system developed using Flask. It demonstrates real-world authentication workflows including registration, login, email verification using OTP, password recovery, role-based authorization, and an admin dashboard.

The project follows the Flask Application Factory Pattern and implements security best practices including password hashing, CSRF protection, environment variables, and rate limiting.

---

# 🚀 Features

## 👤 Authentication

    - User Registration
    - Secure Login
    - Logout
    - Password Hashing (Flask-Bcrypt)
    - Session Management
    - Protected Routes

---

## 📧 Email Verification

    - Email OTP Verification
    - OTP Expiry
    - Resend OTP
    - Gmail SMTP Integration

---

## 🔒 Password Recovery

    - Forgot Password
    - OTP Verification
    - Reset Password
    - Password Re-Hashing

---

## 👮 Authorization

    - Role-Based Access Control
    - User Role
    - Admin Role
    - Custom Admin Decorator

---

## 👨‍💼 Admin Dashboard

    - Dashboard
    - View All Users
    - Activate / Deactivate Users
    - Promote User
    - Demote User
    - Prevent Self Role Change
    - Prevent Self Deactivation

---

## 🛡 Security Features

    - Password Hashing
    - CSRF Protection
    - Environment Variables
    - Flask Sessions
    - Rate Limiting
    - Secure Authentication

---

# ⭐ Feature Highlights

    - 🔐 Secure Authentication
    - 📧 OTP Email Verification
    - 🔄 Forgot Password
    - 👨‍💼 Admin Dashboard
    - 👥 User Management
    - 🔑 Password Encryption
    - 🛡 Rate Limiting
    - 🔒 Environment Variables
    - ⚡ Flask Blueprints
    - 📦 Modular Architecture

---

# 🛠 Tech Stack

    | Category | Technology |
    |----------|------------|
    | Backend | Flask |
    | Database | MySQL |
    | ORM | SQLAlchemy |
    | Forms | Flask-WTF |
    | Authentication | Flask-Login |
    | Password Hashing | Flask-Bcrypt |
    | Email | Flask-Mail |
    | Migration | Flask-Migrate |
    | Rate Limiting | Flask-Limiter |
    | Environment Variables | python-dotenv |

---

# 📂 Project Structure

    ```text
    SecureAuth-Pro/
    │
    ├── app/
    │   ├── forms/
    │   ├── models/
    │   ├── routes/
    │   ├── services/
    │   ├── static/
    │   ├── templates/
    │   ├── utils/
    │   ├── extensions.py
    │   └── __init__.py
    │
    ├── migrations/
    ├── images/
    │
    ├── .env.example
    ├── .gitignore
    ├── config.py
    ├── requirements.txt
    ├── run.py
    └── README.md
    ```

---

# ⚙ Installation

## Clone Repository

    ```bash
    git clone https://github.com/AbhayShihora/SecureAuth-Pro.git

    cd SecureAuth-Pro
    ```

---

## Create Virtual Environment

Windows

    ```bash
    python -m venv venv

    venv\Scripts\activate
    ```

Linux/macOS

    ```bash
    python3 -m venv venv

    source venv/bin/activate
    ```

---

## Install Requirements

    ```bash
    pip install -r requirements.txt
    ```

---

## Configure Environment Variables

    Create a `.env` file using `.env.example`.

    Example

    ```env
    SECRET_KEY=your_secret_key

    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    MYSQL_USER=root
    MYSQL_PASSWORD=your_password
    MYSQL_DB=secureauth_pro

    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False

    MAIL_USERNAME=your_email@gmail.com
    MAIL_PASSWORD=your_gmail_app_password
    MAIL_DEFAULT_SENDER=your_email@gmail.com
    ```

---

## Run Database Migration

    ```bash
    flask db upgrade
    ```

---

## Run Application

    ```bash
    python run.py
    ```

or

    ```bash
    flask run
    ```

---

# 📸 Screenshots

## Home Page

```
images/home.png
```

---

## Register Page

```
images/register.png
```

---

## Login Page

```
images/login.png
```

---

## OTP Verification

```
images/otp.png
```

---

## Forgot Password

```
images/forgot.png
```

---

## User Dashboard

```
images/dashboard.png
```

---

## Admin Dashboard

```
images/admin.png
```

---

## User Management

```
images/users.png
```

---

# 🏗 System Architecture

    ```text
                   Browser
                      │
                      ▼
               Flask Application
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
    Authentication   Email Service   Admin Panel
        │             │             │
    Flask-Login    Flask-Mail      RBAC
        │             │
        ▼             ▼
    Password Hash    Gmail SMTP
    (Bcrypt + OTP)
            │
            ▼
    SQLAlchemy ORM
            │
            ▼
    MySQL Database
    ```

---

# 🔄 Application Flow

    ```text
    User Registration
            │
            ▼
    Email OTP Verification
            │
            ▼
    Login
            │
            ▼
    User Dashboard
            │
            ▼
    Forgot Password
            │
            ▼
    Verify Reset OTP
            │
            ▼
    Reset Password
    ```

---

# 📊 Project Status

    | Feature            | Status |
    |----------          |--------|
    | Registration       | ✅ |
    | Login              | ✅ |
    | Email Verification | ✅ |
    | Forgot Password    | ✅ |
    | Admin Dashboard    | ✅ |
    | User Management    | ✅ |
    | Role-Based Access  | ✅ |
    | Deployment         | ✅ |

---

# 📚 Key Learning Outcomes

    - Flask Application Factory
    - SQLAlchemy ORM
    - Flask Blueprints
    - Authentication
    - Authorization
    - Email OTP
    - Session Management
    - Password Hashing
    - Flask-Mail
    - Flask-Migrate
    - Environment Variables
    - Secure Web Development

---

# 🚀 Future Enhancements

    - Profile Update
    - Profile Picture Upload
    - Login History
    - Audit Logs
    - Search Users
    - Pagination
    - REST API
    - Docker
    - CI/CD Pipeline

---

# 🤝 Contributing

    Contributions are welcome.

    1. Fork the repository
    2. Create your feature branch
    3. Commit your changes
    4. Push to the branch
    5. Open a Pull Request

---

# 📄 License

    This project is licensed under the MIT License.

---

# 👨‍💻 Developer

    **Abhay Shihora**

    Master of Computer Applications (MCA)

    Backend Developer | Python | Flask | SQL | MySQL

📧 Email

    shihoraabhay@gmail.com

💼 LinkedIn

    www.linkedin.com/in/abhayshihora

💻 GitHub

    https://github.com/AbhayShihora

---

# ⭐ Support

    If you found this project helpful, consider giving it a ⭐ on GitHub.

    It helps others discover the project and motivates future improvements.

---

<p align="center">

    Made with ❤️ using Flask & MySQL

</p>
# 🔐 SecureAuth Pro — Enterprise Authentication & User Management System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Flask-3.1-black?style=for-the-badge&logo=flask">
<img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql">
<img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap">
<img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge">
<img src="https://img.shields.io/badge/Brevo-Email_API-0099ff?style=for-the-badge">
<img src="https://img.shields.io/badge/Render-Deployed-success?style=for-the-badge">

</p>

<p align="center">

<img src="https://img.shields.io/github/stars/AbhayShihora/SecureAuth-Pro?style=for-the-badge">
<img src="https://img.shields.io/github/forks/AbhayShihora/SecureAuth-Pro?style=for-the-badge">
<img src="https://img.shields.io/github/last-commit/AbhayShihora/SecureAuth-Pro?style=for-the-badge">
<img src="https://img.shields.io/github/license/AbhayShihora/SecureAuth-Pro?style=for-the-badge">

</p>

<p align="center">

A production-ready Authentication & User Management System built using Flask following modern backend development practices.

Designed with security, scalability, clean architecture and enterprise-level authentication workflows.

</p>

---

# 🌐 Live Demo

### 🚀 Live Application

**🔗 https://secureauth-pro-mzyz.onrender.com**

---

# 📖 Table of Contents

- Project Overview
- Features
- Tech Stack
- Project Structure
- Installation
- Environment Variables
- Screenshots
- System Architecture
- Application Flow
- Project Status
- Learning Outcomes
- Future Enhancements
- Contributing
- License
- Developer

---

# 📌 Project Overview

SecureAuth Pro is a full-stack authentication and user management system developed using **Flask**.

The project demonstrates enterprise-level authentication workflows including secure registration, email verification using One-Time Password (OTP), login, password recovery, role-based authorization, and a complete administrative dashboard.

The application follows the **Flask Application Factory Pattern**, uses **Blueprint Architecture**, and implements security best practices including password hashing, CSRF protection, environment variables, secure sessions, and OTP expiration.

This project was built to simulate how authentication systems are implemented in real-world production web applications.

---

# 🚀 Core Features

## 👤 Authentication

- ✅ User Registration
- ✅ Secure Login
- ✅ Logout
- ✅ Session Management
- ✅ Protected Routes
- ✅ Password Hashing using Flask-Bcrypt

---

## 📧 Email Verification

- ✅ Email OTP Verification
- ✅ Secure OTP Generation
- ✅ OTP Expiration
- ✅ Resend OTP
- ✅ Brevo Email API Integration

---

## 🔑 Password Recovery

- ✅ Forgot Password
- ✅ OTP Verification
- ✅ Reset Password
- ✅ Secure Password Re-Hashing

---

## 👮 Authorization

- ✅ Role-Based Access Control (RBAC)
- ✅ Admin Role
- ✅ User Role
- ✅ Custom Admin Decorator

---

## 👨‍💼 Admin Dashboard

- ✅ Dashboard Overview
- ✅ View All Users
- ✅ Activate User
- ✅ Deactivate User
- ✅ Promote User to Admin
- ✅ Demote Admin to User
- ✅ Prevent Self Role Change
- ✅ Prevent Self Deactivation

---

## 🛡 Security Features

- ✅ Password Hashing (Bcrypt)
- ✅ CSRF Protection
- ✅ Environment Variables
- ✅ Secure Sessions
- ✅ OTP Expiration
- ✅ Secure Password Reset
- ✅ Role-Based Authorization
- ✅ Protected Routes

---

# ⭐ Feature Highlights

- 🔐 Enterprise Authentication
- 📧 Email Verification
- 🔑 OTP Authentication
- 🔄 Forgot Password Workflow
- 🛡 Role-Based Access Control
- 👨‍💼 Admin Dashboard
- 👥 User Management
- 🔒 Password Encryption
- 📩 Brevo Email API
- ⚡ Flask Blueprints
- 🗂 SQLAlchemy ORM
- 🌐 PostgreSQL Deployment
- 📱 Responsive Bootstrap UI
- 🚀 Production Ready

---

# 💡 Why This Project?

SecureAuth Pro demonstrates how authentication systems are implemented in modern web applications.

The project focuses on:

- Secure authentication
- Clean backend architecture
- Modular Flask design
- Scalable project structure
- Secure email verification
- User authorization
- Production deployment
- Real-world coding practices

It serves as an excellent reference for developers learning Flask authentication and can also be used as a foundation for larger web applications.

---
# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| **Backend Framework** | Flask 3.1 |
| **Programming Language** | Python 3.13 |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Database (Development)** | MySQL |
| **Database (Production)** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Authentication** | Flask-Login |
| **Password Hashing** | Flask-Bcrypt |
| **Forms & Validation** | Flask-WTF |
| **Database Migration** | Flask-Migrate |
| **Email Service** | Brevo Email API |
| **Configuration** | python-dotenv |
| **Deployment** | Render |
| **Version Control** | Git & GitHub |

---

# 📂 Project Structure

```text
SecureAuth-Pro/
│
├── app/
│   │
│   ├── forms/
│   │   └── auth_forms.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── __init__.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── dashboard.py
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── email_service.py
│   │   └── auth_service.py
│   │
│   ├── utils/
│   │   ├── decorators.py
│   │   ├── otp.py
│   │   └── helpers.py
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── auth/
│   │   ├── admin/
│   │   ├── dashboard/
│   │   ├── errors/
│   │   └── base.html
│   │
│   ├── extensions.py
│   ├── config.py
│   └── __init__.py
│
├── migrations/
│
├── images/
│
├── instance/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

---

# ⚙ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/AbhayShihora/SecureAuth-Pro.git

cd SecureAuth-Pro
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a **.env** file in the project root.

Example:

```env
SECRET_KEY=your_secret_key

DATABASE_URL=postgresql://username:password@hostname/database

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=secureauth_pro

BREVO_API_KEY=your_brevo_api_key

MAIL_DEFAULT_SENDER=your_email@example.com
```

> **Note:** Never commit your `.env` file to GitHub. Store all sensitive credentials using environment variables.

---

# 🗄 Database Setup

## Initialize Database

```bash
flask db init
```

---

## Generate Migration

```bash
flask db migrate -m "Initial Migration"
```

---

## Apply Migration

```bash
flask db upgrade
```

---

# ▶ Running the Application

Start the Flask development server:

```bash
python run.py
```

or

```bash
flask run
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

# 🚀 Deployment

The project is deployed on **Render**.

### Production Stack

- 🌐 Render
- 🐘 PostgreSQL Database
- 📧 Brevo Email API
- 🔒 Environment Variables
- ⚡ Gunicorn WSGI Server

Live Demo:

**https://secureauth-pro-mzyz.onrender.com**

---

# 📦 Python Packages Used

- Flask
- Flask-Login
- Flask-WTF
- Flask-Bcrypt
- Flask-Migrate
- Flask-SQLAlchemy
- psycopg2-binary
- python-dotenv
- requests
- gunicorn

---

# 🔍 Code Architecture

The project follows a modular architecture using Flask Blueprints.

Each module has a single responsibility:

- **Forms** → Validation
- **Models** → Database
- **Routes** → Request Handling
- **Services** → Business Logic
- **Utils** → Helper Functions
- **Templates** → User Interface
- **Static** → CSS, JavaScript & Images

This separation keeps the project clean, scalable, and easy to maintain.

---
# 📸 Application Screenshots

> **Note:** Replace the placeholder images below with your actual project screenshots stored inside the `images/` folder.

---

## 🏠 Home Page

<p align="center">
<img src="images/home.png" alt="Home Page" width="90%">
</p>

---

## 📝 User Registration

<p align="center">
<img src="images/register.png" alt="Register Page" width="90%">
</p>

---

## 📧 Email OTP Verification

<p align="center">
<img src="images/email_otp.png" alt="OTP Verification" width="90%">
</p>

---

## 🔑 Login Page

<p align="center">
<img src="images/login.png" alt="Login Page" width="90%">
</p>

---

## 🔄 Forgot Password

<p align="center">
<img src="images/forgot_password.png" alt="Forgot Password" width="90%">
</p>

---

## 🔐 Reset Password

<p align="center">
<img src="images/reset_password.png" alt="Reset Password" width="90%">
</p>

---

## 👤 User Dashboard

<p align="center">
<img src="images/dashboard.png" alt="Dashboard" width="90%">
</p>

---

## 👨‍💼 Admin Dashboard

<p align="center">
<img src="images/admin_dashboard.png" alt="Admin Dashboard" width="90%">
</p>

---

## 👥 User Management

<p align="center">
<img src="images/manage_users.png" alt="User Management" width="90%">
</p>

---

# 🏗 System Architecture

```text
                    ┌──────────────────────┐
                    │      Web Browser     │
                    └──────────┬───────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │     Flask Application    │
                  └──────────┬───────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
 Authentication         Admin Panel          Email Service
        │                    │                    │
        ▼                    ▼                    ▼
 Flask-Login         Role-Based Access       Brevo API
 Flask-Bcrypt             Control               (OTP)
        │
        ▼
 SQLAlchemy ORM
        │
        ▼
 PostgreSQL / MySQL
```

---

# 🔄 Authentication Workflow

```text
                User Registration
                        │
                        ▼
             Email OTP Verification
                        │
                        ▼
                 Account Activated
                        │
                        ▼
                     User Login
                        │
                        ▼
                  User Dashboard
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
Forgot Password                  Logout
         │
         ▼
 Receive OTP via Email
         │
         ▼
 Verify Reset OTP
         │
         ▼
 Reset Password
         │
         ▼
 Login with New Password
```

---

# 🛡 Security Workflow

```text
Password
    │
    ▼
Flask-Bcrypt
(Hashing)
    │
    ▼
Database Storage

────────────────────────────

Email Verification

Generate OTP
     │
     ▼
Send via Brevo API
     │
     ▼
User Enters OTP
     │
     ▼
Validate OTP
     │
     ▼
Activate Account

────────────────────────────

Forgot Password

Generate Reset OTP
      │
      ▼
Email User
      │
      ▼
Verify OTP
      │
      ▼
Reset Password
```

---

# 📊 Project Status

| Module | Status |
|---------|:------:|
| User Registration | ✅ |
| Email Verification | ✅ |
| Login Authentication | ✅ |
| Logout | ✅ |
| Password Hashing | ✅ |
| Forgot Password | ✅ |
| Reset Password | ✅ |
| OTP Verification | ✅ |
| Role-Based Access Control | ✅ |
| Admin Dashboard | ✅ |
| User Management | ✅ |
| Activate / Deactivate Users | ✅ |
| Promote / Demote Users | ✅ |
| Protected Routes | ✅ |
| PostgreSQL Deployment | ✅ |
| Brevo Email API | ✅ |
| Responsive UI | ✅ |
| Production Deployment | ✅ |

---

# 🔥 Project Highlights

This project demonstrates practical backend development concepts used in real-world applications.

### Backend

- Flask Application Factory Pattern
- Blueprint Architecture
- SQLAlchemy ORM
- Secure Authentication
- Modular Code Structure
- Environment-Based Configuration

---

### Authentication

- User Registration
- Secure Login
- Email Verification
- OTP Authentication
- Password Reset
- Session Management
- Role-Based Authorization

---

### Security

- Password Hashing (Bcrypt)
- CSRF Protection
- OTP Expiration
- Protected Routes
- Secure Sessions
- Environment Variables

---

### Database

- SQLAlchemy ORM
- MySQL (Development)
- PostgreSQL (Production)
- Flask-Migrate

---

### Deployment

- Render Cloud Hosting
- Gunicorn WSGI Server
- Brevo Email API
- Production Environment Variables

---

# 📈 Resume Highlights

This project showcases experience with:

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- MySQL
- Bootstrap 5
- Authentication
- Authorization
- OTP Verification
- Admin Dashboard
- User Management
- REST-ready Architecture
- Production Deployment
- Git & GitHub
- Responsive UI Design

# 📚 Key Learning Outcomes

Developing **SecureAuth Pro** provided hands-on experience with modern backend development and secure authentication systems.

### 🐍 Python & Flask

- Flask Application Factory Pattern
- Flask Blueprints
- Modular Project Structure
- Flask Extensions
- Clean Code Organization

---

### 🗄 Database

- SQLAlchemy ORM
- Database Relationships
- Database Migrations
- MySQL Integration
- PostgreSQL Deployment

---

### 🔐 Authentication & Authorization

- User Registration
- Secure Login
- Session Management
- Password Hashing using Flask-Bcrypt
- Email OTP Verification
- Forgot Password Workflow
- Password Reset
- Role-Based Access Control (RBAC)
- Protected Routes

---

### 📧 Email Integration

- Brevo Transactional Email API
- OTP Generation
- OTP Validation
- OTP Expiration
- Resend OTP

---

### 🌐 Deployment

- Render Cloud Deployment
- Environment Variables
- Production Configuration
- Gunicorn WSGI Server

---

### 🎨 Frontend

- Bootstrap 5
- Responsive Design
- Flash Messages
- Form Validation
- Clean UI Components

---

# 💼 Skills Demonstrated

This project demonstrates proficiency in:

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- MySQL
- Bootstrap
- Authentication
- Authorization
- REST-ready Architecture
- Email API Integration
- Production Deployment
- Git & GitHub

---

# 🚀 Future Enhancements

The following features are planned for future releases.

### 👤 User Features

- Profile Update
- Profile Picture Upload
- Change Email
- Change Username
- Account Settings
- Dark Mode

---

### 🔐 Security Features

- Two-Factor Authentication (2FA)
- Google OAuth Login
- GitHub OAuth Login
- Account Lockout
- Login History
- Device Management
- Audit Logs
- Password Strength Meter

---

### 👨‍💼 Admin Features

- Search Users
- Pagination
- Dashboard Analytics
- User Activity Logs
- Admin Notifications
- Export User Reports

---

### ⚙ Backend

- REST API
- JWT Authentication
- Docker Support
- Redis Session Store
- Celery Background Tasks
- API Documentation
- Unit Testing
- GitHub Actions CI/CD

---

# 🏆 Project Achievements

✔ Production Ready Authentication System

✔ Responsive User Interface

✔ Enterprise-Level Authentication Workflow

✔ Email OTP Verification

✔ Secure Password Reset

✔ Role-Based Authorization

✔ Admin Dashboard

✔ User Management

✔ PostgreSQL Production Deployment

✔ Clean & Modular Flask Architecture

---

# 🤝 Contributing

Contributions are always welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature/YourFeature
```

5. Open a Pull Request

Please ensure your code follows clean coding practices and includes appropriate documentation.

---

# 📝 Changelog

## Version 1.0.0

- Initial Release
- User Registration
- Login System
- Email Verification using OTP
- Forgot Password
- Reset Password
- Role-Based Authentication
- Admin Dashboard
- User Management
- PostgreSQL Deployment
- Brevo Email Integration

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

# 🙋 Frequently Asked Questions (FAQ)

### Is this project production-ready?

Yes. The project follows Flask best practices and is deployed on Render with PostgreSQL and Brevo Email API.

---

### Which database does it use?

- MySQL (Development)
- PostgreSQL (Production)

---

### Which email service is used?

Brevo Transactional Email API.

---

### Does it support role-based authentication?

Yes.

The application supports separate **Admin** and **User** roles with protected routes and authorization controls.

---

### Can I use this project for learning Flask Authentication?

Absolutely! The project is designed to demonstrate modern authentication workflows and serves as a practical learning resource for Flask developers.

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the creators of:

- Flask
- SQLAlchemy
- Bootstrap
- PostgreSQL
- Brevo
- Render

for providing the tools that made this project possible.

---
# 👨‍💻 Developer

<div align="center">

## Abhay Shihora

**Master of Computer Applications (MCA)**

**Backend Developer | Python | Flask | SQL | PostgreSQL | MySQL**

Passionate about building secure, scalable, and production-ready web applications using modern backend technologies.

</div>

---

# 📬 Contact

<p align="center">

📧 **Email**

**shihoraabhay@gmail.com**

</p>

<p align="center">

💼 **LinkedIn**

https://www.linkedin.com/in/abhayshihora

</p>

<p align="center">

💻 **GitHub**

https://github.com/AbhayShihora

</p>

---

# 🌐 Live Project

### 🚀 SecureAuth Pro

https://secureauth-pro-mzyz.onrender.com

---

# ⭐ Repository Stats

If you found this project useful, please consider:

⭐ Star the repository

🍴 Fork the repository

🐛 Report Issues

💡 Suggest Improvements

Every contribution and star motivates future development.

---

# 🤝 Connect With Me

I'm always open to discussing:

- Python Development
- Flask Projects
- Backend Development
- Open Source
- Software Engineering
- MCA Projects
- Full Stack Development

Feel free to connect!

---

# 💖 Support the Project

If this repository helped you:

⭐ Give it a Star

🍴 Fork it

📢 Share it with others

Your support helps this project grow and motivates future improvements.

---

# 📈 Project Summary

### Project Name

SecureAuth Pro

---

### Project Type

Enterprise Authentication & User Management System

---

### Backend

- Flask
- Python

---

### Database

- PostgreSQL (Production)
- MySQL (Development)

---

### Authentication

- Registration
- Login
- Logout
- OTP Verification
- Forgot Password
- Password Reset

---

### Authorization

- Role-Based Access Control (RBAC)

---

### Admin Features

- Dashboard
- User Management
- Activate / Deactivate Users
- Promote / Demote Users

---

### Email Service

Brevo Transactional Email API

---

### Deployment

Render Cloud Platform

---

### Status

✅ Production Ready

---

# 📜 Project Timeline

```text
Idea
 │
 ▼
Project Planning
 │
 ▼
Database Design
 │
 ▼
Flask Application Factory
 │
 ▼
Authentication System
 │
 ▼
Email OTP Verification
 │
 ▼
Forgot Password
 │
 ▼
Role-Based Access
 │
 ▼
Admin Dashboard
 │
 ▼
User Management
 │
 ▼
Responsive UI
 │
 ▼
PostgreSQL Migration
 │
 ▼
Render Deployment
 │
 ▼
Production Release 🚀
```

---

# 🚀 What's Next?

Upcoming versions will include:

- Google OAuth Login
- GitHub OAuth Login
- REST API
- JWT Authentication
- Docker Support
- Redis Integration
- Profile Management
- Login History
- Audit Logs
- CI/CD Pipeline
- Unit Testing

---

# 🙌 Thank You

Thank you for visiting this repository.

If you have suggestions, feedback, or ideas for improvement, feel free to open an issue or connect with me.

Happy Coding! 🚀

---

<div align="center">

## ⭐ If you like this project, don't forget to Star the Repository!

### Built with ❤️ using

**Python • Flask • SQLAlchemy • PostgreSQL • Bootstrap • Brevo Email API**

</div>
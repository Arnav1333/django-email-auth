# 🔐 User Authentication API with OTP

This project provides a simple and secure Django-based REST API for user authentication using OTP (One-Time Password). It includes user registration with hashed OTPs, token-based login, and environment-based configuration.

## 🚀 Features

- User registration with OTP (One-Time Password)
- OTP sent and stored securely (hashed)
- Login with token generation
- Token-based authentication using DRF
- Environment configuration using `.venv`

## 🛠️ Tech Stack

- Python
- Django
- Django Rest Framework
- SQLite (can be changed to PostgreSQL)


## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Arnav1333/django-email-auth
   cd userauth_api
2. **Create a Virtual Environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
  
3. **Install Dependencies**
   ```bash
    pip install -r requirements.txt

4. **Run Migrations and Run server**
  ```bash
  python manage.py migrate & python manage.py runserver





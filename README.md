# 🏥 Healthcare Backend API

This is a robust and secure backend system for a healthcare management application built using **Django**, **Django REST Framework**, and **PostgreSQL**. The system provides secure user authentication using JWT and supports full CRUD operations for managing patients, doctors, and their mappings.

---

## 📦 Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **Database**: PostgreSQL
- **ORM**: Django ORM

---

## 🚀 Features

- ✅ JWT Authentication (Register & Login)
- ✅ Secure patient and doctor endpoints (only accessible to authenticated users)
- ✅ Full CRUD operations for:
  - Patients
  - Doctors
- ✅ Assign multiple doctors to a patient (Many-to-Many Mapping)
- ✅ Retrieve mappings between patients and doctors
- ✅ Structured project following Django best practices
- ✅ Input validation and error handling
- ✅ Environment-based configuration using `.env`

---

## 🧑‍💻 Setup Instructions

1. go to the Restoring Database.txt file 

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Pravin-Kumar-21/HealthCare-Backend
cd healthcare-backend


python3.8 -m venv env
source env/bin/activate  # for Linux/macOS
env\Scripts\activate     # for Windows


pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate


python manage.py runserver



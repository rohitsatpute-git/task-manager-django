# Task Manager Django Backend

This is the backend API for a Task Manager app built with Django and Django REST Framework.

## 🔧 Features

- JWT-based authentication (if integrated with Node)
- Task creation, update, delete, and filtering by user
- Admin panel for superuser
- CORS enabled for frontend communication
- SQLite3 database (for local and minimal production use)

## 🛠️ Technologies Used

- Python 3
- Django 4+
- Django REST Framework
- SQLite (can switch to PostgreSQL for production)
- CORS Headers

## 🚀 Getting Started

### 1. Clone the repository

```bash```
git clone https://github.com/yourusername/task-manager-django.git
cd task-manager-django


# 2. Create virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Apply migrations and run server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# 4. Create superuser for admin
python manage.py createsuperuser



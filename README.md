# Library Management System

A Django-based Library Management System with an admin panel for managing books and users.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Admin Panel](#admin-panel)
- [License](#license)

## About

This project provides an admin panel to manage books and members in a library. It is built using Django and includes features such as book management and user authentication.

## Installation

### Prerequisites
- Python (3.x recommended)
- Django 4.2.20
- mysqlclient 2.2.7
- djangorestframework 3.15.2
- Virtual Environment (optional but recommended)

### Setup
```sh
# Clone the repository
git clone https://github.com/yourusername/library-management.git
cd library-management

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

The admin panel allows librarians to manage books and users efficiently.

## Project Structure
```
/library_management
│-- manage.py
│-- library_app/
│   │-- models.py
│   │-- views.py
│   │-- urls.py
│   │-- admin.py
│   │-- templates/
│-- requirements.txt
│-- README.md
│-- .env
```

## Environment Variables
Create a `.env` file in the project root and add the required variables:
```sh
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## Running the Project
```sh
# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

## Admin Panel

Access the admin panel at:
```
http://127.0.0.1:8000
```
Use the superuser credentials created earlier to log in and manage books and users.

## License

Specify the license (e.g., MIT, Apache) under which your project is distributed.

---

This project is designed to simplify library management through a Django-powered admin panel. 🚀

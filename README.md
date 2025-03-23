# Library Management System

This is an Admin Panel for a Library Management System built using Django. It provides CRUD operations for managing library data.

## Technologies Used
- **Django**: 4.2.20
- **MySQL**: Database for storing library data

## Features
- Admin panel for managing books, authors, and users
- CRUD operations for library records

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/aniketdoke35/LibrayManagementSystem.git
   ```
2. Navigate to the project directory:
   ```sh
   cd LibrayManagementSystem
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Configure MySQL database in `settings.py`.
6. Apply migrations:
   ```sh
   python manage.py migrate
   ```
7. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
8. Run the server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Access the admin panel at `http://127.0.0.1:8000`.
- Log in using the superuser credentials.
- Manage books, authors, and users through the admin interface.


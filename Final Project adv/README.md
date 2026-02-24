Advanced Task Management API
Developed by Hamed Werteni

Project Overview --------------------------------

This project is an Advanced Task Management REST API built using FastAPI and SQLAlchemy.

It allows users to:

Register securely

Login using JWT authentication

Create, read, update, and delete tasks

Filter tasks by completion status

The application follows a clean modular architecture and demonstrates advanced backend development concepts including authentication, database relationships, and secure endpoint protection.

Technologies Used

Python 3

FastAPI

SQLAlchemy

SQLite

Uvicorn

Passlib (bcrypt hashing)

Python-Jose (JWT Authentication)

Project Structure

Final-project-advanced/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── task_controller.py
└── README.md

File Responsibilities:

main.py – Application entry point and router registration

database.py – Database configuration and session management

models.py – SQLAlchemy models (User, Task)

schemas.py – Pydantic schemas for validation

auth.py – JWT authentication and password hashing

task_controller.py – Task CRUD endpoints

Features

User Registration

User Login with JWT Token

Secure Password Hashing (bcrypt)

Create Task

View All User Tasks

Update Task

Delete Task

Filter Tasks by Completion Status

User-Based Task Ownership

Database

The application uses SQLite.

Database file (automatically created):

advanced_tasks.db

Tables:

users

tasks

Relationship:

One user can have multiple tasks

Each task belongs to one user

How to Run the Project

Install dependencies:
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose

Start the server:

uvicorn main:app --reload

Open API documentation in your browser:
http://127.0.0.1:8000/docs

Authentication Flow

Register a new user using /register

Login using /login

Copy the generated access token

Click Authorize in Swagger

Enter: Bearer YOUR_ACCESS_TOKEN

Access protected task endpoints

API Endpoints

User Endpoints:

POST /register – Register new user

POST /login – Login and receive JWT token

Task Endpoints (Authentication Required):

POST /tasks/ – Create task

GET /tasks/ – Get all user tasks

GET /tasks/{task_id} – Get specific task

PUT /tasks/{task_id} – Update task

DELETE /tasks/{task_id} – Delete task

GET /tasks/?completed=true – Filter completed tasks

Security Features

Passwords hashed using bcrypt

JWT-based authentication

Token expiration implemented

Protected endpoints

Strict user-based task ownership

Purpose of the Project

This project demonstrates:

REST API development with FastAPI

Database integration using SQLAlchemy

Secure authentication using JWT

Clean modular architecture

Advanced backend development practices

Author :

Hamed Werteni
Cyber Security & Business Student.
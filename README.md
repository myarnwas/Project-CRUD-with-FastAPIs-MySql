# FastAPI + MySQL CRUD Example

This is a simple CRUD (Create, Read, Update, Delete) project built with **FastAPI** and **MySQL**.  
It demonstrates how to build REST APIs with FastAPI and connect them to a MySQL database using SQLAlchemy.

---

## 🚀 Features
- Create a new user  
- Get all users  
- Get a single user by ID  
- Update a user  
- Delete a user  
- Interactive API docs with Swagger UI  

---

## 🛠️ Tech Stack
- **Python 3.12+**
- **FastAPI**
- **Uvicorn** (ASGI server)
- **SQLAlchemy**
- **MySQL**

---


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
     ```bash
      git clone https://github.com/myarnwas/Project-CRUD-with-FastAPIs-MySql.git
      cd fastapi-mysql-crud

---

## Install dependencies

pip install -r requirements.txt

---

## Configure Database

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost:3306/testdb"

---

## Run the app

uvicorn main:app --reload

---

## 📖 API Documentation

Once the server is running, open:

Swagger UI: 👉 http://127.0.0.1:8000/docs

ReDoc: 👉 http://127.0.0.1:8000/redoc

---

## 📌 Example API Endpoints

POST /users/ → Create a new user

GET /users/ → Get all users

GET /users/{id} → Get user by ID

PUT /users/{id} → Update user

DELETE /users/{id} → Delete user




# 📝 MyList

MyList is a simple full-stack Todo List application built with **React**, **FastAPI**, and **SQLite**. It allows users to securely manage their personal todo lists and tasks.

## ✨ Features

* 🔐 User Authentication (Register & Login)
* 🍪 JWT Authentication using HTTP-only Cookies
* 📋 Create Todo Lists
* 🗑️ Delete Todo Lists
* ➕ Add Tasks to a Todo List
* ✅ Mark Tasks as Completed
* ❌ Delete Tasks
* ✔️ Completed tasks are displayed with a strike-through effect
* 📱 Clean and responsive UI using Tailwind CSS

---

## 🛠️ Tech Stack

### Frontend

* React
* React Router DOM
* Axios
* Tailwind CSS

### Backend

* FastAPI
* SQLModel
* SQLite
* Uvicorn
* Python

---

## 📂 Project Structure

```text
MyList/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── controllers/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   ├── database.py
│   ├── main.py
│   └── requirements.txt
│
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/MyList.git
cd MyList
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## API Features

### Authentication

* Register
* Login
* Logout
* Get Current User

### Todo Lists

* Create Todo List
* Get All Todo Lists
* Get Todo List by ID
* Delete Todo List

### Tasks

* Create Task
* Get Tasks
* Mark Task Complete
* Delete Task

---


## Future Improvements

* ✏️ Rename Todo Lists
* ✏️ Edit Tasks
* 🔍 Search Tasks
* 📅 Due Dates
* 🌙 Dark Mode
* ⭐ Task Priorities





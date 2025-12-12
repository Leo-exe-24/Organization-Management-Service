# Organization Management Service (FastAPI + MongoDB)

A production-ready backend service for managing organizations with
secure admin authentication.\
Built using **FastAPI**, **MongoDB**, **Motor (async driver)**, and
**JWT-based authentication**, this project is lightweight, scalable, and
fully containerized for real-world deployments.

------------------------------------------------------------------------

## 📘 Detailed Description

The Organization Management Service provides a clean and modular backend
architecture designed for secure data handling and efficient async
operations.\
It focuses on:

-   Managing organization records\
-   Authenticating admins using JWT\
-   Ensuring security with hashed passwords\
-   Maintaining high performance using FastAPI + Motor\
-   Achieving easy scalability through Dockerized microservices

This repository is crafted for developers who want a real-world,
ready-to-deploy backend built with modern Python tooling.

### 🔧 Core Highlights

-   **FastAPI**: High-performance async Python framework\
-   **MongoDB + Motor**: Non-blocking, scalable database operations\
-   **JWT Auth**: Secure and stateless admin sessions\
-   **Docker-first design**: Easy deployments across environments\
-   **Integration Tests**: Ensures end-to-end correctness\
-   **Clean Architecture**: Separation of concerns for long-term
    maintainability

------------------------------------------------------------------------

## 🚀 Features

-   CRUD operations for Organizations\
-   JWT-based admin login\
-   Async DB operations using Motor\
-   PBKDF2-SHA256 & bcrypt-style password hashing\
-   Full Docker + Docker Compose setup\
-   Integration test suite\
-   Built-in API documentation via Swagger UI

------------------------------------------------------------------------

## 📁 Project Structure

    Organization_Management_Service/
    ├─ app/
    │  ├─ main.py             # App entry point
    │  ├─ config.py           # Environment settings
    │  ├─ db.py               # MongoDB connection
    │  ├─ utils.py            # Hashing, JWT utilities
    │  ├─ auth.py             # Authentication logic
    │  ├─ crud.py             # DB CRUD operations
    │  ├─ schemas.py          # Pydantic models
    │  └─ routers/
    │     ├─ org.py           # Organization routes
    │     └─ admin.py         # Admin login routes
    │
    ├─ tests/
    │  └─ test.py             # End-to-end integration tests
    │
    ├─ Dockerfile
    ├─ docker-compose.yml
    ├─ requirements.txt
    ├─ .env.example
    ├─ README.md
    └─ DESIGN_BRIEF.md

------------------------------------------------------------------------

## 🐳 Running with Docker (Recommended)

### 1️⃣ Create your `.env` file

``` sh
cp .env.example .env
```

Update `JWT_SECRET` with a secure value.

### 2️⃣ Build & start services

``` sh
docker-compose up --build
```

API docs → **http://127.0.0.1:8000/docs**

------------------------------------------------------------------------

## 💻 Running Locally (Without Docker)

### 1️⃣ Virtual environment

``` sh
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

### 2️⃣ Install requirements

``` sh
pip install -r requirements.txt
```

### 3️⃣ Run MongoDB

``` sh
docker run -d --name local-mongo -p 27017:27017 mongo:6
```

### 4️⃣ Start FastAPI server

``` sh
uvicorn app.main:app --reload --port 8000
```

------------------------------------------------------------------------

## 🧪 Running Integration Tests

``` sh
python -m tests.test
```

Workflow includes:

-   Create organization\
-   Validate creation\
-   Admin login\
-   Rename organization\
-   Delete organization\
-   Confirm deletion

------------------------------------------------------------------------

## 📘 Additional Documentation

See **DESIGN_BRIEF.md** for:
- Architecture explanation  
- Scalability discussion  
- Trade-offs in tech stack  
- Optional improved system design  

-----------------------------------------------------------------------

## 📜 License

Open-source under the MIT License.

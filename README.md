# 🎬 Movie Collection API

A RESTful API built with FastAPI to manage a personal movie collection.
Features JWT authentication, full CRUD operations, search & filtering,
and comprehensive test coverage.

![CI](https://github.com/YOUR_USERNAME/movie-collection-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **CRUD Operations** — Create, Read, Update, Delete movies
- **JWT Authentication** — Secure endpoints with token-based auth
- **Search & Filtering** — Search by title/director, filter by genre
- **Pagination** — Configurable skip/limit on list endpoints
- **Input Validation** — Pydantic schemas with strict validation rules
- **Auto-generated Docs** — Interactive Swagger UI & ReDoc
- **Comprehensive Tests** — 25+ tests with pytest
- **Docker Support** — Containerized with Docker & Docker Compose
- **CI/CD Pipeline** — Automated testing with GitHub Actions

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | Web framework |
| **SQLAlchemy** | ORM / Database |
| **SQLite** | Database engine |
| **Pydantic** | Data validation |
| **JWT (python-jose)** | Authentication |
| **Passlib + Bcrypt** | Password hashing |
| **Pytest** | Testing |
| **Docker** | Containerization |
| **GitHub Actions** | CI/CD |

---

## 📁 Project Structure
movie-collection-api/
├── app/
│ ├── main.py # Application entry point
│ ├── config.py # Environment configuration
│ ├── database.py # Database connection & session
│ ├── models/ # SQLAlchemy models
│ │ ├── movie.py
│ │ └── user.py
│ ├── schemas/ # Pydantic validation schemas
│ │ ├── movie.py
│ │ └── user.py
│ ├── routers/ # API route handlers
│ │ ├── movie.py
│ │ └── auth.py
│ ├── services/ # Business logic layer
│ │ ├── movie.py
│ │ └── user.py
│ └── auth/ # Authentication utilities
│ ├── utils.py
│ └── dependencies.py
├── tests/ # Test suite
│ ├── conftest.py
│ ├── test_auth.py
│ ├── test_movies.py
│ └── test_health.py
├── .github/workflows/ # CI/CD pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env


---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/movie-collection-api.git
cd movie-collection-api
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your settings
```
5. Run the server
```bash
uvicorn app.main:app --reload
```

6. Open the docs
```bash
http://127.0.0.1:8000/docs
```

7. Docker
```bash
docker-compose up --build
```
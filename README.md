# Creator Directory API

A Django REST Framework (DRF) backend application for managing creators across multiple agencies with secure multi-tenancy, role-based access control, pagination, filtering, sorting, and subscription plan restrictions.

---

# Features

- Multi-tenancy (Agency-based data isolation)
- Role-Based Access Control (Owner, Admin, Member)
- Creator CRUD APIs
- User Management APIs
- Creator Linking & Unlinking
- Agency-specific Notes
- Free Plan Creator Limit
- Pagination
- Filtering
- Sorting
- Automated API Tests
- RESTful API Design

---

# Tech Stack

- Python 3
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Custom Header Authentication

---

# Authentication

Authentication is implemented using a custom request header.

Example:

```http
X-User-Id: u1
```

Example users:

| User | Role |
|------|------|
| u1 | Owner |
| u2 | Admin |
| u5 | Member |

---

# Setup

## Clone Repository

```bash
git clone <repository-url>
cd creator-directory-api
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Database Migrations

```bash
python manage.py migrate
```

## Start Development Server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

---

# Run Tests

```bash
python manage.py test
```

---

# API Endpoints

## Users

| Method | Endpoint |
|---------|----------|
| GET | /api/users/ |
| POST | /api/users/ |

---

## Creators

| Method | Endpoint |
|---------|----------|
| GET | /api/creators/ |
| POST | /api/creators/ |
| GET | /api/creators/{id}/ |
| PATCH | /api/creators/{id}/ |
| DELETE | /api/creators/{id}/ |

---

## Creator Linking

| Method | Endpoint |
|---------|----------|
| POST | /api/creators/{id}/link/ |

---

# Filtering

Filter by niche

```http
GET /api/creators/?niche=travel
```

Filter by minimum followers

```http
GET /api/creators/?min_followers=10000
```

---

# Sorting

Highest followers first

```http
GET /api/creators/?ordering=-follower_count
```

Highest engagement first

```http
GET /api/creators/?ordering=-engagement_rate
```

---

# Pagination

First page

```http
GET /api/creators/?page=1
```

---

# Project Structure

```
creator-directory-api/
│
├── accounts/
├── creators/
├── creator_directory/
├── venv/
├── manage.py
├── requirements.txt
└── README.md
```

---

# Design Decisions

- Agency data is isolated using the `AgencyLink` model.
- Every API request is scoped to the authenticated user's agency.
- Role-based permissions are implemented using custom DRF permissions.
- Custom Header Authentication is used to simplify testing.
- Pagination, filtering, and sorting are implemented using Django REST Framework utilities.
- Free plan agencies can link a maximum of **5 creators**.

---

# Future Improvements

- JWT Authentication
- Search API
- Docker Support
- Swagger / OpenAPI Documentation
- CI/CD Pipeline
- Redis Caching

---

# Author

**Pawan Kumar Shrivastava**
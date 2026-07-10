# Architecture

## Overview

The Creator Directory API is built using Django REST Framework and follows a layered architecture.

The system supports multiple agencies where every agency can manage its own creators without accessing data belonging to other agencies.

---

# Components

## Accounts App

Responsible for:

- Agency Management
- User Management
- Custom Header Authentication

Models

- Agency
- User

---

## Creators App

Responsible for:

- Creator CRUD
- Creator Linking
- Agency Notes
- Plan Restrictions

Models

- Creator
- AgencyLink

---

# Authentication

Authentication is implemented using a custom DRF authentication class.

Every request must include:

```
X-User-Id: <user_id>
```

The authentication class:

- Reads the header
- Fetches the corresponding user
- Sets `request.user`

---

# Authorization

Role Based Access Control is implemented using a custom permission class.

Roles:

- Owner
- Admin
- Member

Permissions:

| Action | Owner | Admin | Member |
|---------|-------|-------|--------|
| View Creators | ✅ | ✅ | ❌ |
| Create Creator | ✅ | ✅ | ❌ |
| Update Creator | ✅ | ✅ | ❌ |
| Delete Creator | ✅ | ✅ | ❌ |
| Manage Users | ✅ | ✅ | ❌ |

---

# Multi-Tenancy

Each user belongs to exactly one agency.

Creators are connected to agencies using the `AgencyLink` model.

Every creator query is filtered using:

```python
agency_links__agency=request.user.agency
```

This ensures complete agency-level data isolation.

---

# Database Relationships

```
Agency
   │
   ├───────────────┐
   │               │
User          AgencyLink
                    │
                    │
                 Creator
```

Relationship Summary

- One Agency → Many Users
- One Agency → Many AgencyLinks
- One Creator → Many AgencyLinks
- AgencyLink acts as the bridge between Agency and Creator.

---

# Business Rules

## Free Plan

Free agencies can link a maximum of **5 creators**.

## Notes

Notes are stored inside the AgencyLink model so that different agencies can maintain different notes for the same creator.

---

# API Features

- CRUD Operations
- Pagination
- Filtering
- Sorting
- Custom Authentication
- Role-Based Permissions
- API Testing

---

# Testing

The project includes automated API tests for:

- List Creators
- Creator Detail
- Create Creator
- Delete Creator

All tests pass successfully.

---

# Future Improvements

- JWT Authentication
- Docker
- Swagger / OpenAPI
- Search API
- Redis Caching
- CI/CD Pipeline
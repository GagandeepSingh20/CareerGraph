
# CareerGraph

CareerGraph is a backend project for a recruiter-focused candidate ranking platform.

The goal of CareerGraph is to go beyond basic CRUD by allowing recruiters to create jobs, candidates to apply for specific jobs, upload resumes, and then rank applicants using an explainable candidate-job matching engine.

Currently, the project is in active development.

---

## Project Vision

Most beginner backend projects only manage data using CRUD operations.

CareerGraph is being built as a more realistic hiring workflow backend:

- Recruiters can create job postings.
- Candidates can create profiles.
- Candidates can apply to a specific job.
- Candidates can upload resumes.
- The system ranks only the candidates who applied to that job.
- Recruiters can see match scores, matched skills, missing skills, and explanations.
- The final version will include authentication, roles, PostgreSQL, Docker, GraphQL, and automated tests.

---

## Current Features

The current backend supports:

- FastAPI application setup
- Health check endpoint
- Candidate creation
- Candidate listing
- Candidate lookup by ID
- Job creation
- Job listing
- Job lookup by ID
- Pydantic validation
- SQLAlchemy models
- SQLite database for local development
- Duplicate candidate checks using email and LinkedIn URL
- Basic duplicate job prevention

---

## Planned Features

CareerGraph will be extended with:

- Signup and login
- JWT authentication
- Role-based access control
  - Admin
  - Recruiter
  - Candidate
- Demo login for recruiters to quickly test the application
- Candidate job application system
- Resume PDF upload
- Resume text extraction
- Job description based ranking
- Applicant ranking per job
- Explainable matching score
- PostgreSQL database
- Alembic migrations
- Docker and Docker Compose
- Strawberry GraphQL API
- Pytest test suite

---

## Tech Stack

Current stack:

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite

Planned final stack:

- Python
- FastAPI
- Strawberry GraphQL
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- Docker Compose
- Pytest
- JWT Authentication

---

# Library Management System

A RESTful API for managing a library system built with Django and Django REST Framework. This API allows users to perform CRUD operations for books, manage book availability, and incorporates rate limiting to ensure fair usage.

---

## Features

- CRUD operations for books:
  - Add, retrieve, update, and delete books.
- Book details include title, author, genre, publication date, availability, edition, and summary.
- Pagination for listing books.
- Rate limiting to prevent abuse (e.g., 100 requests per minute per client).
- API versioning (`/api/v1/...`).

---

## Tech Stack

- **Backend Framework**: Django 4.2
- **API Framework**: Django REST Framework
- **Database**: SQLite (default) or any supported Django database (e.g., PostgreSQL, MySQL).
- **Dependencies**:
  - `django-filter` (for filtering)
  - `drf-yasg` (for API documentation)
  - Other standard libraries (listed in `requirements.txt`)

---

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TemidayoE/library-management-system.git
   cd lib_mgt
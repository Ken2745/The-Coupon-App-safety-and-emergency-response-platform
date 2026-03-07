# Backend Service

This directory contains the Django-based backend for The Coupon App. It exposes RESTful APIs used by the mobile application and any web frontend.

## Components

* **Django project**: Located at `backend/` with `settings.py`, URL configuration, and WSGI/ASGI servers.
* **App module**: `backend/app/` includes models, views, serializers, forms, and tests.
* **Database**: SQLite is used for development and test; see `db.sqlite3`.

## Setup & Development

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Running Tests

```bash
python manage.py test
```

## Notes

* The backend uses Django REST framework for API serialization.
* Authentication and authorization logic may be implemented in `backend/app/views.py`.
* To explore the database models, check `backend/app/models.py`.

---

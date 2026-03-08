# The Coupon App

The Coupon App is a safety-focused mobile platform disguised as a coupon application to discreetly provide access to safety resources and incident logging. A multi-component repository combining an Android client, a Django API server, and a minimal web interface.

---

## Core Components

| Directory | Purpose | Notes |
|-----------|---------|-------|
| `app/` | **Android mobile application** | Java/Gradle project with UI, services, and ML models. See [app/README.md](app/README.md). |
| `backend/` | **Django backend & API** | Data storage, handles auth, and exposes REST endpoints. See [backend/README.md](backend/README.md). |
| `frontend/` | **Web templates & static assets** | Simple Django templates that use HTMX to call the API. See [frontend/README.md](frontend/README.md). |


---
## Tech Stack

Backend
- Python
- Django
- Django REST Framework
- JWT Authentication

Mobile
- Android (Java)
- Gradle
- TensorFlow Lite
- Porcupine Wake Word Detection

Frontend
- Django Templates
- HTMX

---

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API lives at `http://127.0.0.1:8000/api/`; admin at `/admin/`.

### Android Client

Open `app/` in Android Studio or:

```bash
cd c:\Users\kensh\the-coupon-app
gradlew assembleDebug
```

Configure the base URL (e.g. `http://10.0.2.2:8000/api/` for emulator) then install/run on a device.

### Web UI

No build step. Visit `http://127.0.0.1:8000/` after starting the backend. Templates fetch data with HTMX.

---

## Architecture Overview

Android App
      │
      │ REST API
      ▼
Django Backend
      │
      ▼
Database

## Architecture Highlights

* **Discreet UI** – the mobile app appears as a coupon app, with safe‑exit and hidden PIN navigation.
* **Voice & ML** – uses Porcupine wake words and TensorFlow Lite models stored in `app/src/main/assets/`.
* **REST API** – JWT authentication via `rest_framework_simplejwt`; endpoints managed with DRF viewsets and generic views.
* **Small web frontend** – basic login/register pages and dynamic incident log fetching.

---

## Collaboration

This project was developed collaboratively. Team members contributed across frontend development, backend services, database design, AI integration, and CI/CD setup.
Implemented user stories in Jira to mitigate development risks and organize tasks, actively leveraging Scrum meetings to drive application progress.

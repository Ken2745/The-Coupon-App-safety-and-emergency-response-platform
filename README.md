# The Coupon App

## Overview

The Coupon App is a discreet Android mobile application designed to provide safety resources and emergency support for individuals experiencing intimate partner violence (IPV). To maintain user safety and privacy, the app appears to function as a standard coupon-clipping application while hiding critical safety features behind secure access mechanisms.

This project was developed as a collaborative academic software engineering effort and includes a mobile frontend, backend services, and supporting infrastructure.

## Key Features

* **Discreet Interface**: Masquerades as a coupon application to avoid drawing attention.
* **Secure Access**: Hidden PIN-based navigation embedded within coupon interactions.
* **Emergency Support Tools**:

  * Evidence logging
  * Safety planning resources
  * Local resource directory
* **Voice-Activated Triggers**:

  * Wake-word detection using Porcupine
  * Audio classification using TensorFlow Lite for danger detection
* **Location Awareness**: Optional location services to assist emergency responses.

## Technology Stack

### Mobile Application

* Java (Android)
* Android SDK
* Retrofit (REST API communication)
* TensorFlow Lite (audio classification)
* Porcupine (wake-word recognition)

### Backend

* Django (Python)
* SQLite (development database)
* RESTful APIs

### DevOps / CI (Team Contribution)

* GitLab CI/CD
* Docker (containerized builds and deployment pipelines)

## Project Structure

```
The-Coupon-App/
├── android/          # Android mobile application
├── backend/          # Django backend services
├── .gitlab-ci.yml    # CI/CD pipeline configuration
└── README.md
```

## Installation & Setup

### Android Application

1. Open the `android/` directory in Android Studio.
2. Ensure the Android SDK and required build tools are installed.
3. Build and run the application on an emulator or physical device.

### Backend (Optional)

1. Navigate to the backend directory.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:

   ```bash
   python manage.py migrate
   ```
5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

* Launch the app as you would a standard coupon application.
* Authorized users can access hidden safety features via predefined coupon interactions or voice-based triggers.
* Wake words or key phrases can activate audio monitoring and emergency workflows.

## Collaboration

This project was developed collaboratively. Team members contributed across frontend development, backend services, database design, AI integration, and CI/CD setup.

## Project Status

This project is no longer under active development and is maintained for academic reference and portfolio purposes.

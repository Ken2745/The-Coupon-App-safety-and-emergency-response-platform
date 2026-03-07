# Android Mobile Application

This directory holds the Android client for The Coupon App. The app is written in Java and built with Gradle.

## Key Features

* Discreet coupon interface with hidden safety tools.
* Wake-word detection via Porcupine.
* Audio classification with TensorFlow Lite models (`assets/`).
* REST API communication using Retrofit.

## Project Structure

* `app/src/main/java/` – application source code.
* `app/src/main/res/` – resources (layouts, strings, drawables, etc.).
* `app/src/main/assets/` – ML models and Porcupine keyword files.

## Building

Open the project in Android Studio or run from command line:

```bash
gradlew assembleDebug
```

## Testing

Unit and instrumentation tests are under `app/src/test` and `app/src/androidTest`.

## Notes

* The `build.gradle.kts` at the root of `app/` configures dependencies and ProGuard rules.
* Assets include pre-trained models for voice activity and danger detection.

---

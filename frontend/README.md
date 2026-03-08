# Frontend Templates

This folder contains HTML templates and static assets used by any web frontend that interfaces with the backend.

## Contents

* `templates/` – Django-compatible HTML templates for pages such as login, registration, home, and incident log partials.
* `static/` – CSS styles for the polls app; may be reused or extended for other UI components.

## Usage

Templates are loaded by the Django backend when rendering server-side views. To modify the layout or styling, update the corresponding files here and restart the server.

## Notes

* The `frontend/templates/partials` directory holds fragments included in multiple pages.
* Styles under `frontend/static` follow basic CSS and can serve as examples.

---

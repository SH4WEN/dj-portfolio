# DJ Portfolio

A Django-based portfolio website featuring neumorphic design and interactive elements.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Models](#models)
- [Views](#views)
- [URLs](#urls)
- [Templates](#templates)
- [Static Files](#static-files)
- [Media Files](#media-files)
- [Customization](#customization)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

## Overview

DJ Portfolio is a modern, responsive portfolio website built with Django. It features a neumorphic design aesthetic with interactive elements, including flip animations for profile and project images, and a dark/light theme toggle. The site integrates with Cloudinary for cloud-based media storage and serves static files efficiently through WhiteNoise.

## Features

- **Neumorphic UI Design**: Soft, extruded plastic design style with subtle shadows
- **Dark/Light Theme Toggle**: Automatic theme detection with manual override
- **Interactive Flip Animation**: Profile and project images with flip functionality
- **Responsive Layout**: Works on mobile, tablet, and desktop devices
- **Loading Animations**: Custom loading screen with spinner
- **Cloudinary Integration**: Cloud-based media storage and delivery
- **Contact Form**: Email submission with Django's mail backend
- **PDF CV Download**: Static CV file serving
- **Admin Interface**: Django admin with SimpleUI customization

## Technologies Used

- **Backend**: Django 5.2.3
- **Database**: PostgreSQL (with psycopg2-binary)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS (via CDN), custom CSS
- **Icons**: Lucide Icons
- **Media Storage**: Cloudinary (django-cloudinary-storage)
- **Static Files**: WhiteNoise
- **Environment Variables**: python-dotenv
- **Database Management**: dj-database-url
- **Admin Interface**: django-simpleui
- **Web Server**: Gunicorn

## Project Structure

```
dj-portfolio/
├── .env                    # Environment variables
├── .gitignore
├── README.md
├── build.sh               # Build script
├── manage.py              # Django management script
├── render.yaml            # Render deployment configuration
├── requirements.txt       # Python dependencies
├── main/                  # Main application
│   ├── migrations/        # Database migration files
│   ├── templates/main/    # HTML templates
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # App configuration
│   ├── forms.py          # Django forms
│   ├── models.py         # Data models
│   ├── tests.py          # Test cases
│   ├── urls.py           # URL patterns
│   └── views.py          # View functions
├── portfolio_site/        # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py
├── static/               # Static files (CSS, JS, images)
│   ├── main/
│   │   ├── cv/           # CV PDF files
│   │   └── logo.png
│   └── sleep.png         # Default image for flip animation
├── media/                # Uploaded media files (local development)
│   ├── certificates/     # Certificate images
│   └── profile_pics/     # Profile pictures
└── staticfiles/          # Collected static files
```

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd dj-portfolio
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:

   ```env
   SECRET_KEY=your_django_secret_key
   DATABASE_URL=your_database_url
   CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_api_secret
   EMAIL_HOST_USER=your_email_address
   EMAIL_HOST_PASSWORD=your_email_app_password
   DEFAULT_FROM_EMAIL=your_email_address
   CONTACT_EMAIL=recipient_email_for_contact_forms
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Collect static files**

   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## Troubleshooting

### Common Issues

1. **Static Files Not Loading**

   - Run `python manage.py collectstatic`
   - Check `STATIC_ROOT` and `STATICFILES_DIRS` settings

### Debugging Tips

- Enable DEBUG mode in settings for detailed error messages
- Check Django logs for specific error details
- Use browser developer tools to inspect elements and network requests
- Verify environment variables are properly loaded

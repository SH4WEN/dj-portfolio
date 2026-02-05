# DJ-Portfolio - Personal Portfolio Website

A modern, responsive portfolio website built with Django featuring neumorphic design aesthetics and dark/light theme support.

## 🚀 Features

### Core Functionality

- **Responsive Design**: Mobile-first approach with collapsible sidebar
- **Theme Switching**: Light/dark mode with system preference detection
- **Neumorphic UI**: Soft, modern design with depth effects
- **User Authentication**: Admin login/logout functionality
- **Portfolio Sections**: Home, About, Projects, Certificates, Contact

### Technical Features

- Django backend with template inheritance
- Tailwind CSS for styling
- Lucide icons for consistent iconography
- LocalStorage for theme and sidebar state persistence
- Responsive breakpoints for all device sizes
- Accessible UI with proper focus states

## 📁 Project Structure

```
dj-portfolio/
├── main/                    # Main Django app
│   ├── templates/main/     # HTML templates
│   │   ├── base.html       # Base template with sidebar
│   │   ├── home.html       # Home page
│   │   ├── about.html      # About page
│   │   ├── projects.html   # Projects showcase
│   │   ├── certificates.html # Certifications
│   │   └── contact.html    # Contact form
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Form definitions
│   ├── models.py          # Database models
│   ├── urls.py            # URL routing
│   └── views.py           # View functions
├── portfolio_site/        # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI deployment
├── staticfiles/          # Static assets
├── manage.py             # Django management script
└── README.md             # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- Django 4.0+
- pip (Python package manager)

### Quick Start

1. **Clone the repository**

```bash
git clone <repository-url>
cd dj-portfolio
```

2. **Create virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install django
```

4. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

6. **Start development server**

```bash
python manage.py runserver
```

7. **Access the application**

- Local: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 🎨 Design System

### Neumorphic Design Tokens

The project uses a consistent neumorphic design system:

```css
:root {
  --neu-bg: #ecf0f3; /* Light background */
  --neu-bg-accent: #e6eaee; /* Accent background */
  --neu-text: #2b2f36; /* Primary text */
  --neu-primary: #3b82f6; /* Brand color */
  --neu-radius: 16px; /* Border radius */
}
```

### Color Palette

- **Primary**: Blue (#3b82f6)
- **Success**: Green (#16a34a)
- **Warning**: Amber (#f59e0b)
- **Danger**: Red (#dc2626)
- **Dark Mode**: Slate/Gray variants

### Typography

- **Font Family**: Inter (Google Fonts)
- **Font Weights**: 300, 400, 500, 600, 700
- **Base Size**: 16px with responsive scaling

## 📱 Responsive Breakpoints

| Device  | Breakpoint     | Sidebar Behavior             |
| ------- | -------------- | ---------------------------- |
| Mobile  | < 768px        | Hidden by default, slides in |
| Tablet  | 768px - 1024px | Collapsible                  |
| Desktop | > 1024px       | Always visible, collapsible  |

## 🔧 Configuration

### Settings.py Key Configurations

```python
# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main/templates'],
        'APP_DIRS': True,
        # ...
    }
]
```

### Environment Variables

Create a `.env` file for sensitive configurations:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set secure `SECRET_KEY`
- [ ] Configure database settings
- [ ] Set up static file serving
- [ ] Configure SSL/HTTPS
- [ ] Set up proper logging

### Render.com Deployment

The project includes `render.yaml` for easy deployment:

1. Connect your GitHub repository to Render
2. Render will automatically detect and deploy the Django app
3. Configure environment variables in Render dashboard

### Static Files in Production

```python
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## 🎯 Customization Guide

### Adding New Pages

1. Create template in `main/templates/main/`
2. Add view function in `main/views.py`
3. Configure URL pattern in `main/urls.py`
4. Add navigation link in `base.html`

### Modifying Theme

Update CSS variables in `base.html`:

```css
:root {
  --neu-primary: #your-color-here;
  --neu-bg: #your-background-color;
}
```

### Extending Functionality

- Add new models in `main/models.py`
- Create forms in `main/forms.py`
- Implement views in `main/views.py`
- Update templates as needed

## 🔒 Security Considerations

### Best Practices Implemented

- CSRF protection on forms
- Secure password handling
- Proper session management
- XSS prevention through template escaping

### Production Security

- Use environment variables for secrets
- Implement proper authentication
- Regular security updates
- Database backup strategy

## 🤝 Contributing

### Development Workflow

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Code Standards

- Follow PEP 8 for Python code
- Use meaningful variable names
- Include docstrings for functions
- Write descriptive commit messages

## 📞 Support

### Common Issues

**Sidebar not collapsing:**

- Check JavaScript console for errors
- Verify Lucide icons are loading
- Ensure localStorage is enabled

**Theme not persisting:**

- Check browser localStorage permissions
- Verify JavaScript is not blocked
- Clear browser cache and try again

**Mobile layout issues:**

- Test on actual mobile devices
- Check viewport meta tag
- Verify responsive breakpoints

### Getting Help

- Check browser developer tools
- Review Django error logs
- Consult Tailwind CSS documentation
- Refer to Lucide icons documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Lucide Icons](https://lucide.dev/) - Beautiful icon library
- [Django](https://www.djangoproject.com/) - Python web framework
- [Inter Font](https://rsms.me/inter/) - Typography

## 📈 Future Enhancements

### Planned Features

- [ ] Blog section with markdown support
- [ ] Project filtering and search
- [ ] Image gallery with lightbox
- [ ] Contact form email integration
- [ ] Analytics dashboard
- [ ] Progressive Web App (PWA) support
- [ ] Multi-language support (i18n)

### Performance Improvements

- [ ] Image optimization
- [ ] Lazy loading implementation
- [ ] CSS minification
- [ ] JavaScript bundling
- [ ] Caching strategies

---

**Built with ❤️ using Django, Tailwind CSS, and modern web technologies**

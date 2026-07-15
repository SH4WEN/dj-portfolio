from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import About, Profile, Project, Certificate, Skill
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import FileResponse



# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

# Cloudinary is automatically configured via settings.py
# The CloudinaryField should handle URL generation properly


def home(request):
    profile = Profile.objects.first()  # Get the first profile
    projects = Project.objects.all().order_by('-created_at')[:2]  # Only get the 2 latest projects
    skills = Skill.objects.all().order_by('order')
    return render(request, 'main/home.html', {
        'profiles': Profile.objects.all(),
        'skills': skills,
        'projects': projects,  # This now contains only the 2 latest projects
    })

def about(request):
    try:
        about_content = About.objects.prefetch_related('educations', 'work_experiences').first()
    except About.DoesNotExist:
        about_content = None
    
    context = {
        'about': about_content
    }
    return render(request, 'main/about.html', context)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def certificates(request):
    try:
        certificates = Certificate.objects.all().order_by('-date_issued')  # Newest first
        context = {
            'certificates': certificates,
            'count': certificates.count()  # For debugging
        }
        return render(request, 'main/certificates.html', context)
    except Exception as e:
        print(f"Error in certificates view: {e}")  # Check your server logs
        return render(request, 'main/certificates.html', {'certificates': []})

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             try:
#                 # Get form data
#                 name = form.cleaned_data['name']
#                 email = form.cleaned_data['email']
#                 subject = form.cleaned_data['subject']
#                 message = form.cleaned_data['message']

#                 # Send via Django SMTP (Gmail app password configured in .env)
#                 email_subject = f"Portfolio Contact: {subject}"
#                 email_message = f"""New message from your portfolio contact form:

# Name:    {name}
# Email:   {email}
# Subject: {subject}

# Message:
# {message}
# """
#                 msg = EmailMessage(
#                     subject=email_subject,
#                     body=email_message,
#                     from_email=settings.EMAIL_HOST_USER,
#                     to=[settings.CONTACT_EMAIL],
#                     reply_to=[email],  # so you can reply directly to the visitor
#                 )
#                 msg.send(fail_silently=False)

#                 messages.success(request, 'Your message has been sent successfully!')
#                 return redirect('contact')  # Redirect to clear the form
#             except Exception as e:
#                 messages.error(request, 'There was an error sending your message. Please try again later.')
#                 print(f"Email sending error: {e}")  # For debugging
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = ContactForm()

#     return render(request, 'main/contact.html', {'form': form})

def contact(request):
    form_disabled = True  # Change to False to enable the form

    if request.method == 'POST':
        if form_disabled:
            messages.error(request, "The contact form is currently unavailable.")
            return redirect('contact')

        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                email_subject = f"Portfolio Contact: {subject}"
                email_message = f"""New message from your portfolio contact form:

Name:    {name}
Email:   {email}
Subject: {subject}

Message:
{message}
"""

                msg = EmailMessage(
                    subject=email_subject,
                    body=email_message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[email],
                )
                msg.send(fail_silently=False)

                messages.success(request, "Your message has been sent successfully!")
                return redirect('contact')

            except Exception as e:
                messages.error(request, "There was an error sending your message.")
                print(e)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {
        "form": form,
        "form_disabled": form_disabled,
    })
    
def download_cv(request):
    """
    Serve static CV file for download
    """
    # Define the path to the CV file
    cv_filename = "SARMIENTO SHERWIN Q.pdf"
    cv_path = os.path.join(settings.STATIC_ROOT, 'main', 'cv', cv_filename)
    
    # Alternative path in static directory
    if not os.path.exists(cv_path):
        cv_path = os.path.join(settings.STATICFILES_DIRS[0], 'main', 'cv', cv_filename)
    
    # If not found, raise 404
    if not os.path.exists(cv_path):
        raise Http404("CV not found")
    
    try:
        # Serve the file for download
        response = FileResponse(
            open(cv_path, 'rb'),
            content_type='application/pdf'
        )
        response['Content-Disposition'] = f'attachment; filename="{cv_filename}"'
        return response
    except Exception as e:
        raise Http404(f"CV could not be served: {str(e)}")

def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirects to URL named 'home'

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'main/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return '/admin/'
        return super().get_success_url()
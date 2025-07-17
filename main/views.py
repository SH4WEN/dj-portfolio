from django.shortcuts import render
from .models import About, Profile, Project, Certificate, Skill
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

# def home(request):
#     profile = Profile.objects.first()  # Get the first profile
#     return render(request, 'main/home.html', {'profiles': Profile.objects.all()})

def home(request):
    profile = Profile.objects.first()  # Get the first profile
    projects = Project.objects.all().order_by('-created_at')[:4] 
    skills = Skill.objects.all().order_by('order')
    return render(request, 'main/home.html', {
        'profiles': Profile.objects.all(),
        'skills': skills,
        'projects': Project.objects.all(),
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Prepare email content
            email_subject = f"New Contact Form Submission: {subject}"
            email_message = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            Message: {message}
            """
            
            # Send email
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],  # Your email where you want to receive messages
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})



def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirects to URL named 'home'
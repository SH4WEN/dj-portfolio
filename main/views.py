from django.shortcuts import render
from .models import About, Profile, Project, Certificate

def home(request):
    profile = Profile.objects.first()  # Get the first profile
    return render(request, 'main/home.html', {'profiles': Profile.objects.all()})

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
    return render(request, 'main/contact.html')
import os
import django
from django.conf import settings
from django.test import RequestFactory
from django.http import HttpResponseRedirect, Http404

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import Cloudinary
import cloudinary

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET']
)

# Import the download view
from main.views import download_cv

# Import models
from main.models import Profile

# Create a mock request
factory = RequestFactory()

# Test the download view
try:
    print("Testing download_cv view...")
    
    # Create a mock request
    request = factory.get('/download-cv/')
    
    # Call the view
    response = download_cv(request)
    
    print(f"Response type: {type(response)}")
    print(f"Response status code: {response.status_code}")
    
    if isinstance(response, HttpResponseRedirect):
        print(f"Redirect URL: {response.url}")
        print("Download view is working correctly!")
    else:
        print("Unexpected response type")
        
except Http404 as e:
    print(f"HTTP 404 error: {e}")
    # This is expected if no CV is found
    profile = Profile.objects.first()
    if profile:
        if profile.cv:
            print("Profile exists and has CV, but download failed")
        else:
            print("Profile exists but has no CV")
    else:
        print("No profile found")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
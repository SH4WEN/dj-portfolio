import os
import django
from django.conf import settings
from django.http import HttpResponseRedirect

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

# Import models
from main.models import Profile

# Test the download logic
try:
    # Get the profile
    profile = Profile.objects.first()
    
    if profile and profile.cv:
        print(f"Profile CV public ID: {profile.cv.public_id}")
        print(f"Profile CV URL: {profile.cv.url}")
        
        # Test our download logic
        cv_url = profile.cv.url
        print(f"Using URL for download: {cv_url}")
        
        # Create a mock response like our view would
        response = HttpResponseRedirect(cv_url)
        response['Content-Disposition'] = 'attachment'
        
        print(f"Response status code: {response.status_code}")
        print(f"Response location: {response['Location']}")
        print(f"Response Content-Disposition: {response.get('Content-Disposition')}")
        
    else:
        print("No profile or CV found")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
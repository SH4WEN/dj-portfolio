import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import Cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET']
)

# Import models
from main.models import Profile

# Test CV URL construction
try:
    # Get the profile
    profile = Profile.objects.first()
    
    if profile and profile.cv:
        print(f"Profile CV public ID: {profile.cv.public_id}")
        print(f"Profile CV URL: {profile.cv.url}")
        
        # Test Cloudinary config
        cloud_name = cloudinary.config().cloud_name
        print(f"Cloud name: {cloud_name}")
        
        # Construct proper URL for raw files
        cv_url = f"https://res.cloudinary.com/{cloud_name}/raw/upload/{profile.cv.public_id}"
        print(f"Constructed CV URL: {cv_url}")
        
        # Test if we can access the URL
        import requests
        response = requests.head(cv_url)
        print(f"URL status code: {response.status_code}")
        
    else:
        print("No profile or CV found")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
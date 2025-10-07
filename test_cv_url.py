import os
import django
import cloudinary

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

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
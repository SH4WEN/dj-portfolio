import os
import django
from django.conf import settings

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

# Check the exact URL format
try:
    # Get the profile
    profile = Profile.objects.first()
    
    if profile and profile.cv:
        print(f"Profile CV public ID: {profile.cv.public_id}")
        print(f"Profile CV direct URL: {profile.cv.url}")
        
        # Check if version is in the URL
        if 'upload/v' in profile.cv.url:
            print("URL contains version number")
        else:
            print("URL does not contain version number")
            
        # Try to construct the URL manually with version
        cloud_name = cloudinary.config().cloud_name
        public_id = profile.cv.public_id
        manual_url = f"https://res.cloudinary.com/{cloud_name}/raw/upload/v1/{public_id}"
        print(f"Manually constructed URL: {manual_url}")
        
        # Test if manual URL works
        import requests
        response = requests.head(manual_url)
        print(f"Manual URL status code: {response.status_code}")
        
    else:
        print("No profile or CV found")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
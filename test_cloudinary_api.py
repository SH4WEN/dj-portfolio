import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import Cloudinary
import cloudinary
import cloudinary.api

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET']
)

# Import models
from main.models import Profile

# Test Cloudinary API access
try:
    # Get the profile
    profile = Profile.objects.first()
    
    if profile and profile.cv:
        print(f"Profile CV public ID: {profile.cv.public_id}")
        
        # Try to get resource info using Cloudinary API
        public_id = profile.cv.public_id
        resource_info = cloudinary.api.resource(public_id, resource_type='raw')
        
        print(f"Resource info keys: {resource_info.keys()}")
        if 'secure_url' in resource_info:
            print(f"Secure URL: {resource_info['secure_url']}")
        if 'url' in resource_info:
            print(f"URL: {resource_info['url']}")
        if 'bytes' in resource_info:
            print(f"File size: {resource_info['bytes']} bytes")
            
        # Test accessing the file
        import requests
        download_url = resource_info.get('secure_url', resource_info.get('url'))
        if download_url:
            response = requests.get(download_url)
            print(f"Download URL status code: {response.status_code}")
            print(f"Download URL content length: {len(response.content)}")
            
    else:
        print("No profile or CV found")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
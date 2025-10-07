import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import models
from main.models import Profile

# Check the exact URL that will be used for download
try:
    # Get the profile
    profile = Profile.objects.first()
    
    if profile and profile.cv:
        print(f"Profile CV public ID: {profile.cv.public_id}")
        print(f"Profile CV direct URL: {profile.cv.url}")
        
        # Test the actual URL
        import requests
        response = requests.head(profile.cv.url)
        print(f"Actual URL status code: {response.status_code}")
        
        # Also test with HTTPS
        https_url = profile.cv.url.replace('http://', 'https://', 1)
        print(f"HTTPS URL: {https_url}")
        response_https = requests.head(https_url)
        print(f"HTTPS URL status code: {response_https.status_code}")
        
    else:
        print("No profile or CV found")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
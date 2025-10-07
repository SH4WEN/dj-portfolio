import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import models
from main.models import Profile

# Test PDF download
try:
    # Get the profile
    profile = Profile.objects.first()
    
    if profile and profile.cv:
        print(f"Profile CV public ID: {profile.cv.public_id}")
        print(f"Profile CV URL: {profile.cv.url}")
        
        # Test getting the file content
        import requests
        response = requests.get(profile.cv.url)
        print(f"Response status code: {response.status_code}")
        print(f"Response content type: {response.headers.get('content-type')}")
        print(f"Response content length: {len(response.content)}")
        
        # Check if it's actually a PDF
        if response.status_code == 200:
            # Check first few bytes for PDF signature
            content = response.content
            if content.startswith(b'%PDF'):
                print("Content is a valid PDF file")
            else:
                print("Content is NOT a valid PDF file")
                print(f"First 10 bytes: {content[:10]}")
                
    else:
        print("No profile or CV found")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
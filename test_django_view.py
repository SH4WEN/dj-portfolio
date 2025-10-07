import os
import django
from django.conf import settings
from django.test import RequestFactory

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import the download view
from main.views import download_cv

# Create a mock request
factory = RequestFactory()

# Test the download view
try:
    print("Testing static CV download view...")
    
    # Create a mock request
    request = factory.get('/download-cv/')
    
    # Call the view
    response = download_cv(request)
    
    print(f"Response type: {type(response)}")
    print(f"Response status code: {response.status_code}")
    print(f"Content-Type: {response.get('Content-Type')}")
    print(f"Content-Disposition: {response.get('Content-Disposition')}")
    
    # Check if it's a FileResponse
    if hasattr(response, 'streaming_content'):
        print("Response has streaming content")
        # Try to read a small part of the content
        content = next(response.streaming_content)
        if content.startswith(b'%PDF'):
            print("Content is a valid PDF")
        else:
            print("Content is not a valid PDF")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
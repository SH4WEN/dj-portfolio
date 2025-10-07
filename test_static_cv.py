import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Test static CV file access
try:
    # Define the path to the CV file
    cv_filename = "Sarmiento,Sherwin.pdf"
    cv_path = os.path.join(settings.STATICFILES_DIRS[0], 'main', 'cv', cv_filename)
    
    print(f"Looking for CV at: {cv_path}")
    print(f"File exists: {os.path.exists(cv_path)}")
    
    if os.path.exists(cv_path):
        # Get file size
        file_size = os.path.getsize(cv_path)
        print(f"File size: {file_size} bytes")
        
        # Check if it's a valid PDF
        with open(cv_path, 'rb') as f:
            header = f.read(4)
            if header.startswith(b'%PDF'):
                print("File is a valid PDF")
            else:
                print(f"File header: {header}")
    else:
        print("CV file not found!")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
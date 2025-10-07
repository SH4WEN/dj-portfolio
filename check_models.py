import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import models
from main.models import Profile

# Check if we can create a profile
try:
    profile = Profile.objects.create(
        name="Test User",
        title="Software Developer"
    )
    print("Successfully created a profile")
    print(f"Profile ID: {profile.id}")
    
    # Check if we can access the CV field
    print(f"CV field exists: {hasattr(profile, 'cv')}")
    
    # Clean up
    profile.delete()
    print("Cleaned up test profile")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
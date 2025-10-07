import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Import models
from main.models import Profile

# Create a test profile with a CV
try:
    # Create a profile if one doesn't exist
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(
            name="Test User",
            title="Software Developer"
        )
        print("Created a new profile")
    else:
        print("Using existing profile")
    
    # Check if CV field exists and is accessible
    print(f"Profile has CV field: {hasattr(profile, 'cv')}")
    print(f"CV value: {profile.cv}")
    
    # Print profile details
    print(f"Profile ID: {profile.id}")
    print(f"Profile name: {profile.name}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
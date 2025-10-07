from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Profile
import os


class CVDownloadTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test profile
        self.profile = Profile.objects.create(
            name="Test User",
            title="Software Developer"
        )
        
    def test_download_cv_view_exists(self):
        """Test that the download CV view exists"""
        response = self.client.get(reverse('download_cv'))
        # Should either return 200 (if CV exists) or 404 (if CV doesn't exist)
        self.assertIn(response.status_code, [200, 404])
        
    def test_home_page_contains_download_link(self):
        """Test that home page contains download CV link when CV exists"""
        # Create a mock CV file
        test_file = SimpleUploadedFile(
            "test_cv.pdf", 
            b"file_content", 
            content_type="application/pdf"
        )
        
        # Update profile with CV
        self.profile.cv = test_file
        self.profile.save()
        
        # Check that home page contains download link
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Download CV')
        
    def test_home_page_no_download_link_without_cv(self):
        """Test that home page doesn't contain download CV link when no CV exists"""
        response = self.client.get(reverse('home'))
        # Should not contain download link when no CV
        self.assertNotContains(response, 'Download CV')
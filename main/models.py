from django.db import models
from django.utils.text import slugify
from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
     # Changed to CloudinaryField
    image = CloudinaryField('image', folder='projects', blank=True, null=True )
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    date_issued = models.DateField()
    credential_url = models.URLField(blank=True, null=True)
    # Changed to CloudinaryField
    image = CloudinaryField('image', folder='certificates', blank=True, null=True)
    
    def __str__(self):
        return self.title
    


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True, default="")
    title = models.CharField(max_length=200, blank=True, default="")
    bio = models.TextField(blank=True, default="")
    
    # Replace ImageField with CloudinaryField for images
    image = CloudinaryField('image', folder='profile_pics', blank=True, null=True)
    
    # Replace FileField with CloudinaryField for files
    cv = CloudinaryField('file', folder='cvs', resource_type='raw', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    """
    Main about me content
    """
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    introduction = models.TextField()
    hobbies_interests = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About Me Content"

    def __str__(self):
        return f"About {self.name}"

class Education(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ('high_school', 'High School'),
        ('senior_high', 'Senior High School'),
        ('college', 'College/University'),
        ('postgrad', 'Postgraduate'),
        ('certification', 'Certification'),
        ('other', 'Other'),
    ]

    about = models.ForeignKey(About, related_name='educations', on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(null=True, blank=True)
    currently_attending = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"

    def __str__(self):
        status = " - Present" if self.currently_attending else f" - {self.end_year}" if self.end_year else ""
        return f"{self.degree} at {self.institution} ({self.start_year}{status})"

class WorkExperience(models.Model):
    about = models.ForeignKey(About, related_name='work_experiences', on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Work Experiences"

    def __str__(self):
        status = "Present" if self.currently_working else self.end_date.strftime("%Y") if self.end_date else ""
        return f"{self.position} at {self.company} ({self.start_date.year} - {status})"
    

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField(default=0, help_text="Percentage value (0-100)")
    order = models.PositiveIntegerField(default=0, help_text="Order in which skills appear")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} ({self.percentage}%)"
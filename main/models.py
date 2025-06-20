from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    date_issued = models.DateField()
    credential_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    
    def __str__(self):
        return self.title
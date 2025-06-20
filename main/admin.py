from django.contrib import admin
from .models import Project, Certificate

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'date_issued')
    search_fields = ('title', 'issuing_organization')
    list_filter = ('date_issued',)
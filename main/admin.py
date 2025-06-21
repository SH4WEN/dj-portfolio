from django.contrib import admin
from .models import Project, Certificate

from .models import About, Education, WorkExperience
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

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'bio')
        }),
        ('Files', {
            'fields': ('image', 'cv')
        }),
    )


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    fields = ('level', 'degree', 'institution', 'start_year', 'end_year', 'currently_attending', 'order')
    ordering = ('order',)

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1
    fields = ('position', 'company', 'start_date', 'end_date', 'currently_working', 'order')
    ordering = ('order',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'updated_at')
    inlines = [EducationInline, WorkExperienceInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'title', 'introduction', 'hobbies_interests')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'level', 'start_year', 'end_year', 'currently_attending')
    list_filter = ('level',)
    search_fields = ('degree', 'institution')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'currently_working')
    search_fields = ('position', 'company')
    list_filter = ('currently_working',)
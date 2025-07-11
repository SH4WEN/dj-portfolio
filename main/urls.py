from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('certificates/', views.certificates, name='certificates'),
    path('logout/', views.custom_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
]
# urls.py
import os
from django.db import router
from django.urls import include, path
from rest_framework import routers
from database.views import CustomUserViewSet, register
from database.views import  PostViewSet
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name= 'database'
urlpatterns = [
    
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('Useradmin', TemplateView.as_view(template_name='Admin.html')),
    path('home', TemplateView.as_view(template_name='main.html'), name='home'),
    path ('login'  , TemplateView.as_view(template_name= 'login.html')),
    path('logout', TemplateView.as_view(template_name="logout.html")),
    path('register', register, name='register'),
    path('interior', TemplateView.as_view(template_name='Interior.html')),
    path('projects', TemplateView.as_view(template_name='projects.html')),
    path('sites', SiteView.as_view(), name='sites')

  
]
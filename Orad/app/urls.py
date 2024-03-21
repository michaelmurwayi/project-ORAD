# urls.py
import os
from django.db import router
from django.urls import include, path
from rest_framework import routers
from app.views import CustomUserViewSet, register
from app.views import  PostViewSet
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
       
    path('', TemplateView.as_view(template_name='main.html'), name='home'),
    path ('login'  , TemplateView.as_view(template_name= 'login.html'), name='login'),
    path('logout', TemplateView.as_view(template_name="logout.html"), name='logout'),
    path('register', register_view, name="register"),
    path('interior', TemplateView.as_view(template_name='Interior.html')),
    path('sites', SiteView.as_view(), name='sites'),
    path('interior.html',interior_view, name='interior_html'),
    path('serve_pdf/<str:filename>/', serve_pdf, name='serve_pdf'),
    
  
]
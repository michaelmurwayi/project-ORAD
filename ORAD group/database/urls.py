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



urlpatterns = [
    
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('Useradmin', TemplateView.as_view(template_name='Admin.html')),
    path('home', TemplateView.as_view(template_name='main.html'), name='home'),
    path ('login'  , TemplateView.as_view(template_name= 'login.html')),
    path('logout', TemplateView.as_view(template_name="logout.html")),
    path('register', register_view, name="register"),
    path('interior', TemplateView.as_view(template_name='Interior.html')),
    path('projects', TemplateView.as_view(template_name='projects.html')),
    path('sites', SiteView.as_view(), name='sites'),
    path('home', TemplateView.as_view(template_name='main.html'), name='home'),
    path('login/',login, name="login"),
    path('logout/',logout, name="logout"),
    # path('register',register_view, name="register"),
    path('interior.html',interior_view, name='interior_html'),
    path('projects.html',project_view, name='projects_html'),
    # path('sites.html',sites_view, name='sites_html'),
    path('serve_pdf/<str:filename>/', serve_pdf, name='serve_pdf'),
    path('fetch', PostViewSet.as_view, name='fetch'),
    path('posts/', PostViewSet.as_view({'post': 'create_post'}), name='create_post'),
    path('upload-file/', upload_file, name='upload_file'),
    path('fetch-documents/', fetch_documents, name='fetch_documents'),
    path('qc-documents/',qc_document, name='qc_documents'),


  
]
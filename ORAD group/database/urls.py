# urls.py
from atexit import register
import os
from django import views
from django.db import router
from django.urls import include, path
from rest_framework import routers
from database.views import *
# from database.views import  PostViewSet
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'login',AuthViewSet, basename='login')
router.register(r'register', AuthViewSet, basename='signup')
router.register(r'fetch', PostViewSet, basename='fetch_post')
router.register(r'posts',PostViewSet, basename='posts')
# router.register(r'post', PostViewSet, basename='post' )
# router.register(r'users', UserViewSet, basename='users')
app_name= 'database'
urlpatterns = [
    path('', include(router.urls)),
    path('login', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('signup/', AuthViewSet.as_view({'post': 'signup'}), name='signup'),   
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('Useradmin', TemplateView.as_view(template_name='Admin.html')),
    path('home', TemplateView.as_view(template_name='main.html')),
    path('register', TemplateView.as_view(template_name='register.html')),

    # path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    # path('signup/',user_signup_view, name='user-signup'),
    # path('login/', user_login_view, name='user-login'),
    # path('upload/', upload_document, name= 'upload-document'),
    # path('documents/',get_documents, name = 'get-documents'),
  
]  + static(settings.MEDIA_URL, document_root=os.path.join(settings.BASE_DIR, 'media'))

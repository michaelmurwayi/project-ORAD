# urls.py
from atexit import register
from django.db import router
from django.urls import include, path
from rest_framework import routers
from database.views import *
# from database.views import UserViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'login',AuthViewSet, basename='login')
router.register(r'register', AuthViewSet, basename='register')
# router.register(r'post', PostViewSet, basename='post' )
# router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls)),
    # path('login', AuthViewSet.as_view({'post': 'login'}), name='login'),
    # path('register', AuthViewSet.as_view({'post': 'register'}), name='register'),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
    # path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    # path('signup/',user_signup_view, name='user-signup'),
    # path('login/', user_login_view, name='user-login'),
    # path('upload/', upload_document, name= 'upload-document'),
    # path('documents/',get_documents, name = 'get-documents'),
   
    # Add other URL patterns as needed
]

# urls.py
from django.urls import path
from .views import UserProfileView, user_login_view

urlpatterns = [
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('login/', user_login_view, name='user-login'),
    # Add other URL patterns as needed
]

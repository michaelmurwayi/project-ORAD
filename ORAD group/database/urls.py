# urls.py
from django.urls import path
from .views import UserProfileView, user_login_view, user_signup_view, upload_document,get_documents

urlpatterns = [
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('signup/',user_signup_view, name='user-signup'),
    path('login/', user_login_view, name='user-login'),
    path('upload/', upload_document, name= 'upload-document'),
    path('documents/',get_documents, name = 'get-documents'),
   
    # Add other URL patterns as needed
]

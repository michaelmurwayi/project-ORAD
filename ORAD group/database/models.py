

from email.policy import default
import profile
from pyexpat import model
from xml.dom.minidom import Document
from django.contrib.auth.models import User

from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from django.utils import timezone
from sqlalchemy import null


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null= True)
    fullname= models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, default='0')
    email= models.CharField(max_length=57)
    is_active= models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)
    
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=False, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    document = models.FileField(upload_to='documents/', null=True)

# class Post(models.Model):
#     uploader = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=False, null=True)
#     title = models.CharField(max_length=200)



# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = CustomUser()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='custom_user_permissions',
#         blank=True,
#     )

#     groups = models.ManyToManyField(
#         Group,
#         related_name='custom_user_groups',  
#         blank=True,
#     )

#     def __str__(self):
#         return self.email

# class Engineer(models.Model):
#     user_id = self.model(email)
#     upload_file = 
    
# class Document(models.Model):
#     title = models.CharField(max_length=256)
#     file = models.FileField(upload_to="documents/")
#     uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     uploaded_at = models.DateField(auto_now_add=True)


#     def __str__(self):
#         return self.title
  
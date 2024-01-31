# serializers.py
from rest_framework import serializers
from database.models import *
# from .models import Document

class CustomUserViewSet(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'fullname','email','phone_number', 'is_active', 'date_joined']
    

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'content', 'published']

# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = ('id', 'title', 'documents', 'uploaded_at')
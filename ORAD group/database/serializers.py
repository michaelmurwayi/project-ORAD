# serializers.py
from rest_framework import serializers
from .models import CustomUser
from .models import Document

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']
        read_only_fields = ['id', 'is_active', 'date_joined']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'documents', 'uploaded_at')
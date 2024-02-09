# serializers.py
from rest_framework import serializers
from database.models import CustomUser, Document

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email','password', 'is_active', 'date_joined']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['title','file', 'uploaded_at' ]
        

# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = ('id', 'title', 'documents', 'uploaded_at')
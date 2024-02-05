# serializers.py
from rest_framework import serializers
from database.models import CustomUser, Post

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email','password', 'is_active', 'date_joined']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    # Assuming `author` is a ForeignKey to CustomUser
    author = CustomUserSerializer(read_only=True)  # Use CustomUserSerializer for nested serialization

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'pub_date', 'document']
        def validate_author(self, value):
            if not value:
              raise serializers.ValidationError("Author must be specified.")
        # Check if the author instance exists
            if not CustomUser.objects.filter(pk=value.pk).exists():
              raise serializers.ValidationError("Invalid author.")
            return value

# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = ('id', 'title', 'documents', 'uploaded_at')
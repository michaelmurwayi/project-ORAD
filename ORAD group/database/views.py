import email
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from django.utils import timezone
from datetime import timedelta
from .serializers import CustomUserSerializer, DocumentSerializer
from django.db.models import Q
from rest_framework.permissions import AllowAny
from .models import Document



@api_view(['POST'])
@permission_classes([AllowAny])
def user_signup_view(request):
    if request.method == 'POST':
        first_name = request.data.get('first_name')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if first_name or email already exists
        if CustomUser.objects.filter(Q(first_name=first_name) | Q(email=email)).exists():
            return Response({'error': 'First name or Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Create a new custom user
            new_user = CustomUser(first_name=first_name, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response({'message': 'Sign-Up Successful!!'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user and user.is_active:
            login(request, user)
            # token, _ = Token.objects.get_or_create(user=user)
            # expiration_threshold = timezone.now() + timedelta(days=1)
            # if token.created < expiration_threshold:
            #     # Regenerate token if it's about to expire
            #     token.delete()
            #     token = Token.objects.create(user=user)
            #     token.created = timezone.now()
            #     token.save()
            return Response( status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserProfileView(RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
@api_view(['POST'])
def upload_document(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_documents(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data)
from argparse import Action
from crypt import methods
import email
from multiprocessing import context
from os import name
import profile
from venv import create
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from django.utils import timezone
from datetime import timedelta
from .serializers import  CustomUserSerializer, PostSerializer
from django.db.models import Q
from rest_framework.permissions import AllowAny

from database.models import *
from django.contrib.auth import authenticate
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
# from http import HTTPMethod
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.shortcuts import render






class AuthViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    @action(detail=False, methods=['POST'], 
            permission_classes=[permissions.AllowAny],
            url_path=r'register'
        )
    def signup(self, request):
        name = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        user = User.objects.create_user(username, email, password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User created successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        # Render the register.html template
        context = {}
        return render(request, 'register.html', context)
    
    @action(detail=False, methods=['POST'], 
            permission_classes=[permissions.AllowAny],
            url_path=r'login',
        )
    def signin(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if the username and password are valid
        user = authenticate(username=username, password=password)
       
        if user is not None:
            # Generate token
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    # class CustomUserViewSet(viewsets.ModelViewSet):
    #     """A view for the custom user model."""
    #     queryset = CustomUser.objects.all().select_related('user')
    #     serializer_class = CustomUserSerializer
    #     permission_classes=[permissions.IsAuthenticated]
    
class PostViewSet(viewsets.ModelViewSet):
        """A view for the post objects."""
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes=[permissions.IsAuthenticated]

        @action(detail=False, methods=['GET'],
            permission_classes=[permissions.AllowAny],
            url_path=r'fetch',
                )
        def fetch_post(self, request):
           posts = Post.objects.filter(author=request.user).order_by("-published")
           serializer = self.get_serializer(posts, many=True)
           return Response(serializer.data)
        
        @action(detail=False, methods=['POST'],
            permission_classes=[permissions.AllowAny],
            url_path=r'posts',
            )
        def create_post(self, request):
           serializer = PostSerializer(data=request.data)
           if serializer.is_valid():
              serializer.save(author=request.user)
              return Response(serializer.data, status=status.HTTP_201_CREATED)
           else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class CustomUserViewSet(viewsets.ModelViewSet):
        authentication_classes=[TokenAuthentication]
        queryset=User.objects.all()
        serializer_class=CustomUser()
        permission_classes=(permissions.IsAuthenticated)

def home_view(request):
    context={}
    return render(request,'home/main.html',context)

def Admin_view(request):
    context={}
    return render(request,"admin/Admin.html",context)

def register_view(request):
    context={}
    return render(request,"register/register.html",context)

def login_view(request):
    context={}
    return render(request,"login/login.html",context)





# @api_view(['POST'])
# @permission_classes([AllowAny])
# def user_signup_view(request):
#     if request.method == 'POST':
#         first_name = request.data.get('first_name')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         # Check if first_name or email already exists
#         if CustomUser.objects.filter(Q(first_name=first_name) | Q(email=email)).exists():
#             return Response({'error': 'First name or Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # Create a new custom user
#             new_user = CustomUser(first_name=first_name, email=email)
#             new_user.set_password(password)
#             new_user.is_active = False
#             new_user.save()
#             return Response({'message': 'Sign-Up Successful!!'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# @api_view(['POST'])
# @permission_classes([AllowAny])  
# def user_login_view(request):
#     if request.method == 'POST':
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(request, email=email, password=password)

#         if user and user.is_active:
#             login(request, user)
#             token, _ = Token.objects.get_or_create(user=user)
#             expiration_threshold = timezone.now() + timedelta(days=1)
#             if token.created < expiration_threshold:
#                 # Regenerate token if it's about to expire
#                 token.delete()
#                 token = Token.objects.create(user=user)
#                 token.created = timezone.now()
#                 token.save()
#             return Response({'token': token.key}, status=status.HTTP_200_OK)  # Return token upon successful login
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  # Return unauthorized status if login failed
#     else:
#         return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# class UserProfileView(RetrieveAPIView):
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user
    
# @api_view(['POST'])
# def upload_document(request):
#     serializer = DocumentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_documents(request):
#     documents = Document.objects.all()
#     serializer = DocumentSerializer(documents, many=True)
#     return Response(serializer.data)
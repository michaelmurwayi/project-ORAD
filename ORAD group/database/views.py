from fileinput import filename
from importlib.metadata import files
from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import redirect, render

# Create your views here.

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import CustomUserSerializer, DocumentSerializer

from database.models import *
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login as internal_login
from django.http import FileResponse
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotFound, FileResponse



def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Add any additional fields as needed

        # Create a new user
        user = CustomUser.objects.create_user(email=email, password=password)
        
        # Log the user in
        internal_login(request, user)
        
        return redirect('home')  # Redi
    #    token, _ = Token.objects.get_or_create(user=user)
    # Expires in one day
    #   refresh = RefreshToken.for_user(user)
    #   return Response({
    #       "token": str(refresh.access_token)}, status=status.HTTP_201_CREATED)
    # elif request.method == "GET":
    #     return render(request, "register.html")
    return render(request, 'register.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            internal_login(request, user)
            return redirect('home')  # Redirect to home page or any other page after successful login
        
        return render(request, 'login.html', {'error_message': 'Invalid username or password.'}) 
    return render(request, 'login.html')
# logout(request)
# return HttpResponseRedirect('/login/')


def logout(request):
    return redirect("login")


# def upload_document(request):
#     if request.method == 'POST':
#         # Handle file upload
#         uploaded_file = request.FILES.get('filled_pdf')
#         if uploaded_file:
#             # Save the uploaded file to the server
#             file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', uploaded_file.name)
#             with open(file_path, 'wb+') as destination:
#                 for chunk in uploaded_file.chunks():
#                     destination.write(chunk)
#             # Perform further processing as needed
#             return JsonResponse({'message': 'File uploaded successfully'}, status=201)
#         else:
#             return JsonResponse({'error': 'No file provided'}, status=400)
#     else:
#         return HttpResponseNotFound()

def serve_pdf(request, filename):
    # Serve the PDF file to the client
    pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'pdf', filename)
    if os.path.exists(pdf_file_path):
        return FileResponse(open(pdf_file_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound()



class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser()
    permission_classes = permissions.IsAuthenticated


def home_view(request):
    context = {}
    return render(request, "home/main.html", context)


def Admin_view(request):
    context = {}
    return render(request, "admin/Admin.html", context)


def register_view(request):
    context = {}
    return render(request, "register.html", context)


def login_view(request):
    context = {}
    return render(request, "login/login.html", context)

def interior_view(request):
    context={}
    return render (request, 'interior.html',context) 

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
#             return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#     def get(self, request):
#         # Render the register.html template
#         context = {}
#         return render(request, 'register.html', context)

#     @action(detail=False, methods=['POST'],
#             permission_classes=[permissions.AllowAny],
#             url_path=r'login',
#         )
#     def login(self, request):
#         fullname = request.data.get('fullname')
#         password = request.data.get('password')

#         # Check if the fullname and password are valid
#         user = authenticate(fullname=fullname, password=password)

#         if user is not None:
#             # Generate token
#             refresh = RefreshToken.for_user(user)
#             return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
#         else:
#             return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class CustomUserViewSet(viewsets.ModelViewSet):
#     """A view for the custom user model."""
#     queryset = CustomUser.objects.all().select_related('user')
#     serializer_class = CustomUserSerializer
#     permission_classes=[permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    """A view for the post objects."""

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=[permissions.AllowAny],
        url_path=r"posts",
    )
    def create_post(self, request):
        serializer = DocumentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
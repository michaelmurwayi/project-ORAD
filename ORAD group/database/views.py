import email
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view

@api_view(['POST'])
def api_login(request):
    email = request.data['Email']
    password = request.data['Password']
    user = authenticate(email=email)
    if user is not None and user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200)
    else:
        return Response({'error':'Invalid Credentials'}, status=status.HTTP_401)
    
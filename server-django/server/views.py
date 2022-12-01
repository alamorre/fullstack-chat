from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

import requests

@api_view(['POST'])
def signup(request):
    username = request.data['username']
    secret = request.data['secret']
    email = request.data['email']
    first_name = request.data['first_name']
    last_name = request.data['last_name']

    user = User.objects.create(
        username=username, 
        email=email, 
        password=make_password(secret),
        first_name=first_name, 
        last_name=last_name
    )

    response = requests.post('https://api.chatengine.io/users/', 
        data={
            "username": username,
            "secret": secret,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        },
        headers={ "Private-Key": "49a46286-91c3-4f9c-92bf-284ae51b7628" }
    )

    return Response(response.json(), status=response.status_code)
    
@api_view(['POST'])
def login(request):
    username = request.data['username']
    secret = request.data['secret']

    user = get_object_or_404(User, username=username)
    if not user.check_password(secret):
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    response = requests.get('https://api.chatengine.io/users/me/', 
        headers={ 
            "Project-ID": "5d498a31-cd23-42b7-b367-4fcc9463bd2f",
            "User-Name": username,
            "User-Secret": secret
        }
    )

    return Response(response.json(), status=response.status_code)
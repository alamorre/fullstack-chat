from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests

import environ
env = environ.Env()
environ.Env.read_env()

@api_view(['POST'])
def signup(request):
    username = request.data['username']
    secret = request.data['secret']
    email = request.data['email']
    first_name = request.data['first_name']
    last_name = request.data['last_name']

    # user = User.objects.create(
    #     username=username, 
    #     email=email, 
    #     password=make_password(secret),
    #     first_name=first_name, 
    #     last_name=last_name
    # )

    response = requests.post('https://api.chatengine.io/users/', 
        data={
            "username": username,
            "secret": secret,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        },
        headers={ "Private-Key": env('CHAT_ENGINE_PRIVATE_KEY') }
    )

    return Response(response.json(), status=response.status_code)
    
@api_view(['POST'])
def login(request):
    username = request.data['username']
    secret = request.data['secret']

    # user = get_object_or_404(User, username=username)
    # if not user.check_password(secret):
    #     return Response({}, status=status.HTTP_404_NOT_FOUND)

    response = requests.get('https://api.chatengine.io/users/me/', 
        headers={ 
            "Project-ID": env('CHAT_ENGINE_PROJECT_ID'),
            "User-Name": username,
            "User-Secret": secret
        }
    )

    return Response(response.json(), status=response.status_code)
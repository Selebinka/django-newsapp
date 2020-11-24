import requests
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CreateUserSerializer
from .utils import get_client_id_and_client_secret

if get_client_id_and_client_secret(name='BaseAuth'):
    CLIENT_ID, CLIENT_SECRET = get_client_id_and_client_secret(name='BaseAuth')
else:
    CLIENT_ID = CLIENT_SECRET = None


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "password"}
    """
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        # Then we get a token for the created user.
        # This could be done differentley
        response = requests.post('{}/o/token/'.format(settings.BASE_URL),
                                 data={
                                     'grant_type': 'password',
                                     'username': request.data['username'],
                                     'password': request.data['password'],
                                     'client_id': CLIENT_ID,
                                     'client_secret': CLIENT_SECRET,
                                 },
                                 )
        print(response)
        return Response(response.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "password"}
    """
    response = requests.post(
        '{}/o/token/'.format(settings.BASE_URL),
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(response.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    response = requests.post(
        '{}/o/token/'.format(settings.BASE_URL),
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(response.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    response = requests.post(
        '{}/o/revoke_token/'.format(settings.BASE_URL),
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return success message (would be empty otherwise)
    if response.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, response.status_code)
    # Return the error if it goes badly
    return Response(response.json(), response.status_code)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

from .models import CustomUser

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, "user":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, "username": user.username, "email": user.email}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


@api_view(['POST'])
def check_authentication(request):
    if request.method == 'POST':
        token = request.data.get('token')
        if token:
            try:
                token_obj = Token.objects.get(key=token)
                if token_obj:
                    user = token_obj.user
                    return Response({'message': 'User is authenticated', 'username': user.username, 'email': user.email}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Token is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
            except Token.DoesNotExist:
                return Response({'error': 'Token is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)
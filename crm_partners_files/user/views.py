from django.contrib.auth import get_user_model
from django.http import Http404
from jwt import ExpiredSignatureError
from jwt.exceptions import DecodeError
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from passlib.apps import django_context
from django.conf import settings

from custom_exceptions.not_authorized_exception import AuthorizationError

User = get_user_model()


class CustomTokenObtainPairView(APIView):
    """
    Create JWT token and get user data depends on jwt token stored data(username).
    Returns object with tokenData and userData fields.
    """
    permission_classes = [AllowAny, ]

    def get_user(self, username):
        """
        Get user data depends on jwt token stored data(username).
        """
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None

    def create_token(self, user):
        """
        JWT token creation method. Use simple jwt app to create token.
        """
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = self.get_user(username=username)
            if user == None:
                return Response({'error': 'User does not exist'},
                                status=status.HTTP_404_NOT_FOUND)

            hash = user.password
            is_validated = django_context.verify(password, hash)
            if not is_validated:
                return Response({'error': 'Password is not valid'},
                                status=status.HTTP_401_UNAUTHORIZED)

            token_data = self.create_token(user)
            return Response(
                {'tokenData': token_data},
                status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserData(APIView):
    def get_user_id_from_jwt_token(self, request):
        """
        Get user id from JWT token
        """
        jwt_authenticator = JWTAuthentication()
        response = jwt_authenticator.authenticate(request)
        if response is not None:
            return response[1]['id']
        else:
            raise AuthorizationError('Token is not valid')

    def get_user_from_database(self, id):
        """
        Get user from database.
        """
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            raise Http404('User not found')

    def get(self, request, format=None):
        try:
            # getting user id
            user_id = self.get_user_id_from_jwt_token(request)

            # getting user from database
            user = self.get_user_from_database(user_id)

            return Response({'username': user.username})
        except Http404 as error:
            return Response({'error': str(error)}, status.HTTP_404_NOT_FOUND)
        except AuthorizationError as error:
            return Response({'error': str(error)})
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

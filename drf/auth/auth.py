from django.http import HttpResponse
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import AccessToken

from django.contrib.auth.models import User

from utils.decorators import error_handler


class CookieJWTAuth(JWTAuth):
    def __call__(self, request):
        token = request.COOKIES.get('access_token')
        if token and 'HTTP_AUTHORIZATION' not in request.META:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'

        return super().__call__(request)


class DrfJwtAuth(BaseAuthentication):
    @error_handler
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None
        
        token = auth_header.split(' ')[1]
        
        try:
            validated_token = AccessToken(token)
            user_id = validated_token['user_id']
            user = User.objects.get(id=user_id)
            
            return user, validated_token
            
        except Exception as e:
            raise AuthenticationFailed('Неверный токен аутентификации')


def set_access_cookie(response: HttpResponse, access: str) -> None:
    response.set_cookie(
        'access_token',
        access,
        httponly=True,
        samesite='Lax',
        secure=False,
        max_age=7 * 24 * 60 * 60,
    )




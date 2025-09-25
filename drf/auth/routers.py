import logging
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import path

from ninja import Router, NinjaAPI
from ninja.errors import HttpError
from ninja_jwt.tokens import AccessToken

from auth.schemas import AuthInput, UserOut
from auth.auth import set_access_cookie

from utils.decorators import error_handler


logger = logging.getLogger('auth')

api = NinjaAPI()
router = Router()


class JWTAuthorization:
    @router.post('register', response={201: UserOut})
    @error_handler
    @staticmethod
    def register(request, payload: AuthInput, response: HttpResponse):
        username = payload.username.strip()
        if not username or not payload.password:
            raise HttpError(400, 'username и password обязательны')
        if User.objects.filter(username=username).exists():
            raise HttpError(400, 'Такой пользователь уже существует')

        user = User.objects.create_user(username=username, password=payload.password)
        access = str(AccessToken.for_user(user))
        set_access_cookie(response, access)

        logger.info(f"Пользователь {user} зарегистрировался.")

        return 201, UserOut(id=user.id, username=user.username)

    @router.post('login', response=UserOut)
    @error_handler
    @staticmethod
    def login(request, payload: AuthInput, response: HttpResponse):
        user = authenticate(username=payload.username.strip(), password=payload.password)
        if not user:
            raise HttpError(401, 'Неверный логин или пароль.')

        access = str(AccessToken.for_user(user))
        set_access_cookie(response, access)

        logger.info(f"Пользователь {user} вошел в систему.")

        return UserOut(id=user.id, username=user.username)

    @router.post('logout')
    @error_handler
    @staticmethod
    def logout(request, response: HttpResponse):
        response.delete_cookie('access_token')

        logger.info(f"Пользователь c id {request.user.id} вышел из системы")

        return {'detail': 'Успешный выход из системы.'}


api.add_router(prefix='auth/', router=router)

urlpatterns = [
    path('', api.urls)
]
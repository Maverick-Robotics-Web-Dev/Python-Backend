from django.conf import settings
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import action
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from cacvsa.settings.base import *
from restapi.support.methods import *
from .serializers import *


class LoginViewSet(GenericViewSet):

    model = UserEmployeeModel
    permission_classes = [AllowAny]
    serializer_class = CustomJwtTokenSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def create(self, request):

        username = request.data.get(
            'user_employee_user_name', None)
        password = request.data.get('password', None)

        status = self.model.objects.filter(
            user_employee_user_name=username).first().user_employee_status
        active = self.model.objects.filter(
            user_employee_user_name=username).first().is_active

        if not status and not active:
            response = {
                'error': 'ERROR',
                'msg': 'No existe el Usuario con esas credenciales'
            }
            return Response(response, HTTP_204_NO_CONTENT)

        user = authenticate(username=username, password=password)

        if user:

            if user.user_employee_login and user.is_authenticated:
                response = {
                    'ok': 'OK',
                    'msg': 'Ya has iniciado sesión',
                    'home': HOME_URL
                }
                return Response(response, HTTP_200_OK)

            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = LoginSerializer(
                    user, data={'user_employee_login': True}, partial=True)
                if user_serializer.is_valid():
                    user_serializer.save()

                access_token = login_serializer.validated_data['access']
                refresh_token = login_serializer.validated_data['refresh']

                if CACV_KEY['SESSION_LOGIN']:
                    django_login(request, user)

                access_token_expiration = (
                    timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
                refresh_token_expiration = (
                    timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
                return_expiration_times = CACV_KEY['JWT_AUTH_RETURN_EXPIRATION']

                if return_expiration_times:
                    data = {
                        'ok': 'OK',
                        'msg': 'Iniciado sesión exitosamente',
                        'access-token': access_token,
                        'refresh-token': refresh_token,
                        'access-expiration': access_token_expiration,
                        'refresh-expiration': refresh_token_expiration,
                        'user': user_serializer.data,
                    }

                data = {
                    'ok': 'OK',
                    'msg': 'Iniciado sesión exitosamente',
                    'access-token': access_token,
                    'refresh-token': refresh_token,
                    'user': user_serializer.data
                }

                # serializer = self.serializer_class(
                #     instance=data, context=self.get_serializer_context())

            response = Response(data, HTTP_200_OK)

            if CACV_KEY['USE_JWT']:
                set_jwt_cookies(response, access_token, refresh_token)
            return response

        response = {
            'error': 'ERROR',
            'msg': 'Usuario o Contraseña Incorrectos'
        }
        return Response(response, HTTP_400_BAD_REQUEST)


class LogoutViewSet(ViewSet):

    def get(self, request, *args, **kwargs):
        if getattr(settings, 'ACCOUNT_LOGOUT_ON_GET', False):
            response = self.logout(request)

        else:
            response = self.http_method_not_allowed(request, *args, **kwargs)

        return self.finalize_response(request, response, *args, **kwargs)

    def logout(self, request):

        if CACV_KEY['SESSION_LOGIN']:
            user_serializer = LoginSerializer(
                request.user, data={'user_employee_login': False}, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
            django_logout(request)

        response = Response(
            {'msg': _('Cerró sesión exitosamente')},
            HTTP_200_OK,
        )

        if CACV_KEY['USE_JWT']:

            cookie_name = CACV_KEY['JWT_AUTH_COOKIE']
            unset_jwt_cookies(response)

            if 'rest_framework_simplejwt.token_blacklist' in settings.INSTALLED_APPS:
                # add refresh token to blacklist
                try:
                    black_token = request.data['refresh-token']
                    token = RefreshToken(black_token)
                    token.blacklist()
                except KeyError:
                    response.data = {'msg': _(
                        'El token de actualización no se incluyó en los datos de la solicitud.')}
                    response.status_code = HTTP_401_UNAUTHORIZED
                except (TokenError, AttributeError, TypeError) as error:
                    if hasattr(error, 'args'):
                        if 'Token is blacklisted' in error.args or 'Token is invalid or expired' in error.args:
                            response.data = {'msg': _(error.args[0])}
                            response.status_code = HTTP_401_UNAUTHORIZED
                        else:
                            response.data = {'msg': _(
                                'Se ha producido un error.')}
                            response.status_code = HTTP_500_INTERNAL_SERVER_ERROR

                    else:
                        response.data = {'msg': _('Se ha producido un error.')}
                        response.status_code = HTTP_500_INTERNAL_SERVER_ERROR

            elif not cookie_name:

                message = _(
                    'Ni las cookies ni la lista negra están habilitadas, por lo que el token '
                    'no se ha eliminado del lado del servidor. Asegúrese de que el token se elimine del lado del cliente.',
                )
                response.data = {'msg': message}
                response.status_code = HTTP_200_OK
        return response

    def create(self, request):
        return self.logout(request)


class PasswordChangeViewSet(GenericViewSet):

    model = UserEmployeeModel
    serializer_class = PasswordChangeSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    @action(['post'], True,)
    def password_change(self, request, pk=None):
        user = self.get_object(pk)
        print(user)
        if user:
            password_serializer = self.serializer_class(data=request.data)
            if password_serializer.is_valid():
                user.set_password(
                    password_serializer.validated_data['password'])
                user.save()
                response = {
                    'ok': 'OK',
                    'msg': 'Cambio de contraseña exitoso'
                }
                return Response(response, HTTP_200_OK)
            else:
                response = {
                    'error': password_serializer.errors,
                    'msg': 'Existen errores en la informaacion enviada'
                }
                return Response(response, HTTP_200_OK)
        else:
            response = {
                'error': 'Error',
                'msg': 'No existe el usuario con esas credenciales'
            }
            return Response(response, HTTP_204_NO_CONTENT)

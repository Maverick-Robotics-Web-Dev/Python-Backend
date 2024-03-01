from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
from rest_framework.authtoken.models import Token as DefaultTokenModel
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from cacvsa.settings.base import *

# sensitive_post_parameters_m = method_decorator(
#     sensitive_post_parameters(
#         'password', 'old_password', 'new_password1', 'new_password2',
#     ),
# )

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(),
)


# def get_token_model():
#     token_model = Token
#     session_login = CACV_KEY['SESSION_LOGIN']
#     use_jwt = CACV_KEY['USE_JWT']

#     if not any((session_login, token_model, use_jwt)):
#         raise ImproperlyConfigured(
#             'No authentication is configured for rest auth. You must enable one or '
#             'more of `TOKEN_MODEL`, `USE_JWT` or `SESSION_LOGIN`'
#         )
#     if (
#         token_model == DefaultTokenModel
#         and 'rest_framework.authtoken' not in INSTALLED_APPS
#     ):
#         raise ImproperlyConfigured(
#             'You must include `rest_framework.authtoken` in INSTALLED_APPS '
#             'or set TOKEN_MODEL to None'
#         )
#     return token_model


# def jwt_encode(user):

#     JWTTokenClaimsSerializer = TokenObtainPairSerializer

#     refresh = JWTTokenClaimsSerializer.get_token(user)
#     print(refresh)
#     return refresh.access_token, refresh


# def default_create_token(token_model, user, serializer):
#     token, _ = token_model.objects.get_or_create(user=user)
#     return token


def set_jwt_access_cookie(response, access_token):

    cookie_name = CACV_KEY['JWT_AUTH_COOKIE']
    access_token_expiration = (
        timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
    cookie_secure = CACV_KEY['JWT_AUTH_SECURE']
    cookie_httponly = CACV_KEY['JWT_AUTH_HTTPONLY']
    cookie_samesite = CACV_KEY['JWT_AUTH_SAMESITE']
    cookie_domain = CACV_KEY['JWT_AUTH_COOKIE_DOMAIN']

    if cookie_name:
        response.set_cookie(
            cookie_name,
            access_token,
            expires=access_token_expiration,
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite,
            domain=cookie_domain,
        )


def set_jwt_refresh_cookie(response, refresh_token):

    refresh_token_expiration = (
        timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
    refresh_cookie_name = CACV_KEY['JWT_AUTH_REFRESH_COOKIE']
    refresh_cookie_path = CACV_KEY['JWT_AUTH_REFRESH_COOKIE_PATH']
    cookie_secure = CACV_KEY['JWT_AUTH_SECURE']
    cookie_httponly = CACV_KEY['JWT_AUTH_HTTPONLY']
    cookie_samesite = CACV_KEY['JWT_AUTH_SAMESITE']
    cookie_domain = CACV_KEY['JWT_AUTH_COOKIE_DOMAIN']

    if refresh_cookie_name:
        response.set_cookie(
            refresh_cookie_name,
            refresh_token,
            expires=refresh_token_expiration,
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite,
            path=refresh_cookie_path,
            domain=cookie_domain,
        )


def set_jwt_cookies(response, access_token, refresh_token):
    set_jwt_access_cookie(response, access_token)
    set_jwt_refresh_cookie(response, refresh_token)


def unset_jwt_cookies(response):
    cookie_name = CACV_KEY['JWT_AUTH_COOKIE']
    refresh_cookie_name = CACV_KEY['JWT_AUTH_REFRESH_COOKIE']
    refresh_cookie_path = CACV_KEY['JWT_AUTH_REFRESH_COOKIE_PATH']
    cookie_samesite = CACV_KEY['JWT_AUTH_SAMESITE']
    cookie_domain = CACV_KEY['JWT_AUTH_COOKIE_DOMAIN']

    if cookie_name:
        response.delete_cookie(
            cookie_name, samesite=cookie_samesite, domain=cookie_domain)
    if refresh_cookie_name:
        response.delete_cookie(refresh_cookie_name, path=refresh_cookie_path,
                               samesite=cookie_samesite, domain=cookie_domain)

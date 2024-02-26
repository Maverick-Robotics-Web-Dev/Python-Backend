from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured
from rest_framework.authtoken.models import Token as DefaultTokenModel
from cacvsa.settings.base import *

# sensitive_post_parameters_m = method_decorator(
#     sensitive_post_parameters(
#         'password', 'old_password', 'new_password1', 'new_password2',
#     ),
# )

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(),
)


def get_token_model():
    token_model = CACV_KEY.TOKEN_MODEL
    session_login = CACV_KEY.SESSION_LOGIN
    use_jwt = CACV_KEY.USE_JWT

    if not any((session_login, token_model, use_jwt)):
        raise ImproperlyConfigured(
            'No authentication is configured for rest auth. You must enable one or '
            'more of `TOKEN_MODEL`, `USE_JWT` or `SESSION_LOGIN`'
        )
    if (
        token_model == DefaultTokenModel
        and 'rest_framework.authtoken' not in INSTALLED_APPS
    ):
        raise ImproperlyConfigured(
            'You must include `rest_framework.authtoken` in INSTALLED_APPS '
            'or set TOKEN_MODEL to None'
        )
    return token_model


def jwt_encode(user):

    JWTTokenClaimsSerializer = CACV_KEY.JWT_TOKEN_OBTAIN_SERIALIZER

    refresh = JWTTokenClaimsSerializer.get_token(user)
    return refresh.access_token, refresh


def default_create_token(token_model, user, serializer):
    token, _ = token_model.objects.get_or_create(user=user)
    return token

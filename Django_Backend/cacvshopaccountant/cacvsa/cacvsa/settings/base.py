"""
Django settings for cacvsa project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from django.core.exceptions import ImproperlyConfigured
import json
from unipath import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).ancestor(3)


def get_cacvsa_file(secret_name):
    try:
        with open("cacvsa.json") as f:
            secret_file = json.loads(f.read())
        return secret_file[secret_name]
    except:
        msg = f'La Variable {secret_name} no existe'
        raise ImproperlyConfigured(msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_cacvsa_file('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'restapi.business',
    'restapi.cashregisters',
    'restapi.clients',
    'restapi.employees',
    'restapi.owners',
    'restapi.products',
    'restapi.suppliers',
    'restapi.users'
]

THIRD_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'coreapi',
    'drf_yasg'
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cacvsa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cacvsa.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

###### Custom Settings #########

AUTH_USER_MODEL = 'users.UserEmployeeModel'
LOGIN_URL = '/api/v1/routes/business/vouchertype'
HOME_URL = '/'
# JWT_TOKEN_OBTAIN_SERIALIZER = 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',

CACV_KEY = {
    'USE_JWT': True,
    'LOGIN_SERIALIZER': 'restapi.auth.serializers.LoginSerializer',
    'JWT_SERIALIZER': 'restapi.auth.serializers.JWTSerializer',
    'JWT_SERIALIZER_WITH_EXPIRATION': 'restapi.auth.serializers.JWTSerializerWithExpiration',
    'JWT_TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
    'JWT_AUTH_COOKIE': 'jwt-cacvsa-auth-token',
    'JWT_AUTH_REFRESH_COOKIE': 'jwt-cacvsa-refresh-token',
    'JWT_AUTH_REFRESH_COOKIE_PATH': '/',
    'JWT_AUTH_SAMESITE': 'Lax',
    'JWT_AUTH_COOKIE_DOMAIN': None,
    'JWT_AUTH_SECURE': False,
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_RETURN_EXPIRATION': False,

    'TOKEN_SERIALIZER': 'restapi.auth.serializers.TokenSerializer',
    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    'TOKEN_CREATOR': 'restapi.support.default_create_token',
    'SESSION_LOGIN': True,
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    # To activate JWT
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication'],

    # The default permission policy may be set globally
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']

}

# SIMPLE_JWT = {
#     'TOKEN_OBTAIN_SERIALIZER': 'restapi.users.serializers.CustomJwtToken'
# }

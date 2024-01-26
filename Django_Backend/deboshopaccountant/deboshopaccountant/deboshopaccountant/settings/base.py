# from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import json
from unipath import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# with open("secret.json") as f:
#     secret_file = json.loads(f.read())

def get_secret_file(secret_name):
    try:
        with open("secret.json") as f:
            secret_file = json.loads(f.read())
        return secret_file[secret_name]
    except:
        msg = "La Variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)


SECRET_KEY = get_secret_file('SECRET_KEY')

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
    'apis.business',
    'apis.cashregisters',
    'apis.clients',
    'apis.employees',
    'apis.owners',
    'apis.products',
    'apis.suppliers',
    'apis.users'
]

THIRD_APPS = [
    'rest_framework',
    'coreapi',
    'rest_framework.authtoken',
    'dj_rest_auth'
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

ROOT_URLCONF = 'deboshopaccountant.urls'

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

WSGI_APPLICATION = 'deboshopaccountant.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.UserEmployeeModel'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    # To activate JWT
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ],

    # The default permission policy may be set globally
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']

}

# REST_AUTH = {
#     'USE_JWT': True,
#     'JWT_AUTH_COOKIE': 'jwt-dsa-auth-token',
#     'JWT_AUTH_REFRESH_COOKIE': 'jwt-dsa-refresh-token',
# }

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'jwt-dsa-auth-token'
JWT_AUTH_REFRESH_COOKIE = 'jwt-dsa-refresh-token'

# To define custom serializers
# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'apis.users.serializers.UserEmployeeSerializer',
# }

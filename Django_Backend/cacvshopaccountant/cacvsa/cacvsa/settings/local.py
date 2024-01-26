from .base import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': get_cacvsa_file('DB_HOST'),
        'PORT': get_cacvsa_file('DB_PORT'),
        'USER': get_cacvsa_file('DB_USER'),
        'PASSWORD': get_cacvsa_file('DB_PW'),
        'NAME': get_cacvsa_file('DB_NAME'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

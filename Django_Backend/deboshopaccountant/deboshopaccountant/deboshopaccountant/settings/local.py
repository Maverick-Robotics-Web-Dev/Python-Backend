from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST' : get_secret_file('DB_HOST'),
        'PORT' : get_secret_file('DB_PORT'),
        'USER' : get_secret_file('DB_USER'),
        'PASSWORD' : get_secret_file('DB_PW'),
        'NAME': get_secret_file('DB_NAME'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
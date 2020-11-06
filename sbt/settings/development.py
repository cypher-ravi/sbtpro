from .base import *


from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS += [
]

MIDDLEWARE += [
]


  
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sbtauth2',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode':'STRICT_TRANS_TABLES',
        },
    }
}



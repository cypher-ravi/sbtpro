
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['164.90.213.239','stacksoftwares.in','www.stacksoftwares.in','127.0.0.1']


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
        'NAME': 'sbtdb',
        'USER': 'sbtadmin',
        'PASSWORD': '2020@SBTadmin',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'sql_mode':'STRICT_TRANS_TABLES',
        },
    }
}


from .base import *

DEBUG = False

ALLOWED_HOSTS = ['164.90.213.239','stacksoftwares.in','www.stacksoftwares.in','127.0.0.1']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'io)y8-71d+8-kn7%*k&dk=4ri$=2&8i=!rvczc7c6m00o7tdno'




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

from .base import *


from .base import *
import json


with open("config.json", "r") as params:
    parameters = json.load(params)

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
        'NAME': 'sbt',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode':'STRICT_TRANS_TABLES',
        },
    }
}



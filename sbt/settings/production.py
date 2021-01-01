
from .base import *
import json

import pathlib 

# path = Path(__file__).parent / ../"config.json"
# / "../sbtproject/SBTProlive/config.json"

fn = pathlib.Path(__file__).parent.parent.parent / 'config.json'
with open(fn,"r") as params:
    parameters = json.load(params)


DEBUG = True

ALLOWED_HOSTS = ['164.90.213.239','sbtprofessionals.com','www.sbtprofessionals.com']
SECRET_KEY = 'io)y8-71d+8-kn7%*k&dk=4ri$=2&8i=!rvczc7c6m00o7tdno'

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
        'NAME': 'sbt',
        'USER': 'sbtliveadmin',
        'PASSWORD': 'XWZ@3Blqwertsbt',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'sql_mode':'STRICT_TRANS_TABLES',
        },
    }
}

"""
Django settings for sbt project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages



# from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

import pymysql
pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'io)y8-71d+8-kn7%*k&dk=4ri$=2&8i=!rvczc7c6m00o7tdno'



# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'website',
    'phonenumber_field',
    'restapi',
    'rest_framework',
    'dashboard',
    'rest_framework_swagger',
    'Vendor',
    'Employee',
    'Customer',
    'django_filters',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sbt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['sbt/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'website.views.menu_top',

            ],
        },
    },
]

WSGI_APPLICATION = 'sbt.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static/")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]
# managing media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Added manually
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "globalstaticfiles"),
    # for production server static settings
    #  '/home/sbtadmin/sbtprojects/static/',
    #  ]

# Added manually Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rk7305758@gmail.com'
EMAIL_HOST_PASSWORD = 'ztupoklvzybovgtd'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'SBT Professional Team <rk7305758@gmail.com>'



MESSAGE_TAGS = {
    messages.ERROR: 'danger',

}

# LOGIN_REDIRECT_URL = 'INDEx'
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert border-0 alert-primary bg-gradient m-b-30 alert-dismissible fade show border-radius-none',
    messages.INFO: 'alert alert-warning alert-dismissible fade show',
}
REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
                   'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
                   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',
                   ]
                   }


AUTH_USER_MODEL = "authentication.User"



#Twilio
# TWILIO_PHONE = config('TWILIO_PHONE', default=None)
# TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default=None)
# TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default=None)


IMPORT_EXPORT_USE_TRANSACTIONS = True

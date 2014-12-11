# -*- coding: utf-8 -*-
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '$&18%-#2nmz1*)07x0wfncdoir#f!oso@#p*6qj^0s0k)bii!b'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads') 
#MEDIA_URL = '/uploads/'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
#дефолтные форматы даты/времени не работают, если тру
USE_L10N = False
USE_TZ = True

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y - H:i:s  O'
TIME_FORMAT = 'H:i:s'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'moddjango',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'main.urls'

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'main/templates/'),
#    os.path.join(BASE_DIR, 'stories/templates/'),
#    os.path.join(BASE_DIR, 'comments/templates/'),
#)

WSGI_APPLICATION = 'main.wsgi.application'

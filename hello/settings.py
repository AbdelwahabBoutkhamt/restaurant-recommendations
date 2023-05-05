"""
Django settings for hello project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x!jvx^n=sen@n$w73d@#(xs5lb-=8@x!z#04ze7+u+zfz(@d&1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',  # for google
    # social app settings
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # providers of allauth are
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',

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

ROOT_URLCONF = 'hello.urls'




#Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.in'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'davidsmith2831@gmail.com'
EMAIL_HOST_PASSWORD = 'UL1nD8hu2hYU'
DEFAULT_FROM_EMAIL = 'davidsmith2831@gmail.com'
SERVER_EMAIL = 'davidsmith2831@gmail.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'hello.wsgi.application'

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 261736975254482 -app id
# f9c3b49f47669fbb0e6e8af6cf909e5b -app secret

# 716306222920-nr2mlidb9urthbud2o9rh5odofr0iivd.apps.googleusercontent.com -google cliet id
# 5dOLk4BEguN2AsHmP_1LckXx  -google secret key


# SOCIAL_AUTH_FACEBOOK_KEY = '261736975254482'  # Facebook App	ID
# SOCIAL_AUTH_FACEBOOK_SECRET = 'f9c3b49f47669fbb0e6e8af6cf909e5b'  # Facebook App Secret

# SOCIAL_AUTH_GITHUB_KEY = '6a1fbb8ae329f1ab1785'  # github id
# SOCIAL_AUTH_GITHUB_SECRET = 'e050c43066705ebd71603ee536b5b3c978eb278f'  # github secret key

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# soial app change settings


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 1

# tages of message overide

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# added manualy by me
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

]

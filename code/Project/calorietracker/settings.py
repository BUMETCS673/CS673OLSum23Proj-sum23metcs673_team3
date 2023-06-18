"""
Django settings for calorietracker project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# -----------------

#For Custom Google Auth Function
#from pathlib import Path
#from google.oauth2 import id_token


# Google OAuth configuration
# GOOGLE_CLIENT_ID = ''
# GOOGLE_CLIENT_SECRET = '='
#GOOGLE_AUTH_REDIRECT_URI = '/'

#------------------
# SITE_ID = 1

# AUTHENTICATION_BACKENDS = [
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',

#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]
ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/foods/'
LOGIN_URL="/login/"

#custom user model
# AUTH_USER_MODEL = 'login.User'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zzkc1$6@s7au3bisaakx$c=y*fb2vy$(fl+8$l+7s+9hc!bae+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Add ip address of test client machine here
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['192.168.29.25','localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'login',
    'debug_toolbar', 
    'bootstrap5',
    'foods',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google',
    'social'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend'

    

]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'calorietracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/"templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'calorietracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#TODO: Write a guide for setting up the DB locally so it can be connected to, for now just comment this out to test without the db connection
DATABASES = {
    "default": {
        "NAME":"calorie_tracker", # Postgres dbName
        "ENGINE": "django.db.backends.postgresql",
        "HOST":"localhost",
        "USER": 'postgres', # Local Postgres usrname
        "PASSWORD":"password" # Local Postgres passwd
        # "OPTIONS": {
        #     "passfile": ".pgpass",
        # },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

# Email sending function
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587


EMAIL_HOST_USER = 'cs673team3@gmail.com' 
EMAIL_HOST_PASSWORD = 'vkfyympkkcobgbnn' # Will figure out a way for security issue
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True

#Media Folders
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

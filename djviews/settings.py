"""
Django settings for djviews project.

Generated by 'django-admin startproject' using Django 4.2.6.

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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1iif0tcbolf-=+y$f+)rgjkbuo)gcxr%(-5+7e9iyyz5gxvd@_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
Login_URL = '/login'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_results',
    'django_hosts',

    'blog',
    'products',
    'blog_two',
    'products_two',
    'dashboard',
    'blog_three',
    'djtemp',
    'accounts',
    'cars',
    'billing',
]

AUTH_USER_MODEL = "accounts.MyUser"

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'djviews.urls'
ROOT_HOSTCONF = 'djviews.hosts'
DEFAULT_HOST = 'www'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'djviews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SHORTCODE_MIN = 25


# from dotenv import load_dotenv
# load_dotenv()


# # REDIS SETTINGS
# REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
# FULL_URL = os.getenv('FULL_URL')
# REDIS_URL = os.getenv('REDIS_URL')
# HOST = os.getenv('HOST')
# PORT = os.getenv('PORT')
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": FULL_URL,
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "PASSWORD": REDIS_PASSWORD,
#             "SSL": True,
#         }
#     }
# }

# # Test REDIS cache
# from django.core.cache import cache
# cache.set('test_key', 'Redis test_value', timeout=60) # Set a value in the cache
# value = cache.get('test_key') # Retrieve the value
# print(value) # Output should be "Redis test_value"


# import redis
# def check_redis_connection():
#     try:
#         redis_client = redis.StrictRedis(host=HOST, port=PORT, password=REDIS_PASSWORD)    
#         # Test the connection
#         if redis_client.ping():
#             print('Connected to Redis')
#             return True
#         else:
#             print('Could not connect to Redis')         
#             return False
#     except Exception as e:
#         print(f'An error occurred: {e}')
# check_redis_connection()


# # CELERY SETTINGS
# CELERY_BROKER_URL = FULL_URL
# CELERY_RESULT_BACKEND = FULL_URL
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE # 'Africa/Cairo'
# CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
# CELERY_IMPORTS = ("billing.tasks",)

# # check celery connection
# import socket
# def check_port(ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((ip, port))
#     if result == 0:
#         print(f"Celery port : {port} is open")
#     else:
#         print(f"Celery port : {port} is not open")
#     # return result
#     sock.close()
# check_port(HOST, int(PORT))
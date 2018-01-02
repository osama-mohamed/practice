from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'OSAMA',
        'PASSWORD': 'OSAMA',
        'HOST': '',
        'PORT': '',
    }
}


try:
    from .local import *
except:
    pass

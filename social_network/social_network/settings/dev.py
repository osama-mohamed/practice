from .base import *


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

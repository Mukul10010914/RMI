from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']
SECRET_KEY = 'django-insecure-q))ikg(!j1vc1goy25qp8_u+kwzxjca%dwt_ej-mmbnhha*=ny'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rim',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
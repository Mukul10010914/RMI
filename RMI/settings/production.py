from .base import *
import os
from dotenv import load_dotenv
import random

dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'.env')
load_dotenv(dotenv_path)

ALLOWED_HOSTS = ['54.185.2.112']
SECRET_KEY = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
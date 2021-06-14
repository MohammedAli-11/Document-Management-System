from .base import *

SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1', '*']

DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
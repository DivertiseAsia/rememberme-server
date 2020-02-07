from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', default='PLEASE_SET_DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ORIGIN_URL = 'http://localhost'
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rememberme',
        'USER': 'postgres',
        'PASSWORD': '1234567q',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SUPER_PASSWORD = 'RememberME1234'

SENDGRID_API_KEY = 'SG.PLEASE_ADD_SENDGRID_API_KEY'
DEV_EMAIL = 'dev@divertise.asia'
ADMIN_EMAIL = 'fah@divertise.asia'

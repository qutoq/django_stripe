from pathlib import Path
import environ
import os

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('django_key')
STRIPE_SECRET_KEY = env('secret_key')
SECRET_WEBHOOK = env('secret_webhook')
DOMAIN = env('DOMAIN')
DEBUG = env('DEBUG')
#ALLOWED_HOSTS = [env('HOST')]

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'shop',
    'cart'
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

ROOT_URLCONF = 'django_stripe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

#CSRF_TRUSTED_ORIGINS = ['https://*.eu.ngrok.io', 'https://*.127.0.0.1', 'https://localhost', 'http://0.0.0.0:8']
CSRF_TRUSTED_ORIGINS = ['http://*', 'http://localhost:1337']
WSGI_APPLICATION = 'django_stripe.wsgi.application'
CART_SESSION_ID = 'cart'



#DATABASES = {
#    "default": {
#        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
#        "USER": os.environ.get("SQL_USER", "user"),
#        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#        "HOST": os.environ.get("SQL_HOST", "localhost"),
#        "PORT": os.environ.get("SQL_PORT", "5432"),
#    }
#}

DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "NAME": env("SQL_DATABASE"),
        "USER": env("SQL_USER"),
        "PASSWORD": env("SQL_PASSWORD"),
        "HOST": env("SQL_HOST"),
        "PORT": env("SQL_PORT"),
    }
}




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



#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = bool(env("EMAIL_USE_TLS"))
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")



LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "staticfiles/media"

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = 'static/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/media')
#MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
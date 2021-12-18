import os
from pathlib import Path
import environ
import django_heroku

env = environ.Env()
environ.Env.read_env()

def get_var(key, default=False):
    try: return env(key)
    except: return default

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'xeb+m#$-(xm8swac=sf3-zx#609=j)q*qb_7c^w52x3fl5#6jm'

DEBUG = get_var("DEBUG", True)

INSTALLED_APPS = [
    'door',
    'exam',
    'student',
    'teacher',
    'auth_api',
    'evaluation',
    'subscription',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mainsias_dj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mainsias_dj.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static_django/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_storage/')
MEDIA_URL = '/media/'

STATIC_ROOT=os.path.join(BASE_DIR, 'static')
# AWS S3 configuration

AWS_ACCESS_KEY_ID = get_var("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_var("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_var("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'

DEFAULT_FILE_STORAGE = 'mainsias_dj.storage_backends.MediaStorage'

# Razor Pay API configurations

RAZORPAY_API_KEY_ID = get_var("RAZORPAY_API_KEY_ID", "rzp_test_blLxeoG2nMlmq9")
RAZORPAY_API_KEY_SECRET = get_var("RAZORPAY_API_KEY_SECRET")


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# Coustom default User Model 

AUTH_USER_MODEL = 'auth_api.User'


# Email Configuration

EMAIL_HOST = get_var("EMAIL_HOST", "smtp.gmail.com")
DEFAULT_FROM_EMAIL = get_var("DEFAULT_FROM_EMAIL")
EMAIL_HOST_USER = get_var("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_var("EMAIL_HOST_PASSWORD")
EMAIL_PORT = get_var("EMAIL_PORT", "587")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
    CORS_ALLOWED_ORIGINS = [
        'https://mainsias.com',
        'https://api.mainsias.com',
        'https://evaluators.in',
        'https://api.evaluators.in'
    ]
    ALLOWED_HOSTS = ['mainsias.com', 'api.mainsias.com', 'evaluators.in', 'api.evaluators.in']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': get_var("DATABASE_NAME"),
            'USER': get_var("DATABASE_USER"),
            'HOST': get_var("DATABASE_HOST"),
            'PORT': get_var("DATABASE_PORT"),
            'PASSWORD': get_var("DATABASE_PASSWORD"),
        }
    }

#Activate Django-Heroku
django_heroku.settings(locals())
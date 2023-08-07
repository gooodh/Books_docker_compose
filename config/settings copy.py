from pathlib import Path
import os
import socket


from environs import Env
env = Env()  # new
env.read_env()  # new

SECRET_KEY = env("DJANGO_SECRET_KEY", 'django-insecure-@16-ebmc&6$33skoq*ye!+3mu(6-os^rkrz6j%ch=e6&wc01m8')
# DEBUG = env.bool("DJANGO_DEBUG", True)
DEBUG = True 

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['93.189.147.166', 'localhost', '127.0.0.1']  # new

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # new
    # Third-party
    'crispy_forms',  # new
    'crispy_bootstrap4',
    'allauth',  # new
    'allauth.account',  # new
    'debug_toolbar',  # new
    # Local
    'accounts',
    'pages',
    'books',  # new
]

AUTH_USER_MODEL = 'accounts.CustomUser'  # new
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'  # new


CRISPY_TEMPLATE_PACK = 'bootstrap4'  # new


SITE_ID = 1
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'allauth.account.auth_backends.AuthenticationBackend',  # new
)

ACCOUNT_SESSION_REMEMBER = True # new
ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True # new
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # new

MEDIA_URL = '/media/' # new
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))  # new

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',  # new
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # new
    'django.middleware.cache.FetchFromCacheMiddleware',  # new
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('POSTGRES_HOST', 'db_books'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        }
}

# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 'NAME': 'postgres',
# 'USER': 'postgres',
# 'PASSWORD': '123456789qwert',
# 'HOST': 'db_books',
# 'PORT': '5432'
# }
# }


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = 'staticfiles'
STATIC_URL = 'static/'


STATICFILES_DIRS=[(os.path.join(BASE_DIR,'static'))]


STATICFILES_FINDERS = [
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com'



hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]


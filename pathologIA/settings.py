from pathlib import Path
import os, mimetypes
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jun@-jc+e*c^c^e3&rch*!$eb&q+phu1h!*%)+wkd%5!f9idh&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['3.82.249.240', '*']
# Custom Configuration

LOGIN_URL = '/login/'
AUTH_USER_MODEL = 'AccountsApp.CustomUserModel'


# Application definition

INSTALLED_APPS = [
    'AccountsApp.apps.AccountsappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HomeApp.apps.HomeappConfig',
    'CasesApp.apps.CasesappConfig',
    'ImagesApp.apps.ImagesappConfig',
    'QuestionsApp.apps.QuestionsappConfig',
    'ResultsApp.apps.ResultsappConfig',
    'VideosApp.apps.VideosappConfig',
    'StudentsApp.apps.StudentsappConfig',
    'DemarcateApp.apps.DemarcateappConfig',
    'PredictionApp.apps.PredictionappConfig',
    'ForumApp.apps.ForumappConfig',
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'AccountsApp.backends.EmailBackend',
    ]


ROOT_URLCONF = 'pathologIA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'pathologIA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': 'sql.cnf',
#         },
#     }
# }

# DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': dj_database_url.parse(
        "mysql://root:qfRYeLRdlRrcGaZrLlzrOMoRGwzaTZaN@switchback.proxy.rlwy.net:41268/railway",
        conn_max_age=600
    ),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'pathologIA/static/')
]

mimetypes.add_type("text/css", ".css", True)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MODEL_ROOT = os.path.join(BASE_DIR, 'modelos')
MODEL_URL = '/modelos/'

CMODEL_ROOT = os.path.join(BASE_DIR, 'cmodelos')
CMODEL_URL = '/cmodelos/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

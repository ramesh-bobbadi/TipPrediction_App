import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_AL_HOSTNAME')]

CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('RENDER_EXTERNAL_AL_HOSTNAME')]
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware',]
CORS_ALLOWED_ORIGINS = []
STORAGES ={
    "default": {
        "BACKEND" :"django.core.files.storage.FileSystemStorage",
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    }
}

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
    )
}

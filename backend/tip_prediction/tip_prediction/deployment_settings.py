import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [
    "tipprediction-app-3.onrender.com",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "https://tipprediction-app-3.onrender.com",
    "https://tip-prediction-app-deud-i2rclybce-application-developers.vercel.app",
]
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
 
CORS_ALLOWED_ORIGINS = [
    "https://tip-prediction-app-deud-i2rclybce-application-developers.vercel.app",
]
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

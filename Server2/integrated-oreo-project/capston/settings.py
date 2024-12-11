"""
Django settings for capston project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os, allauth
# from django.contrib.auth.models import AbstractUser

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2h(qwsvw^06bogj=9*+)0#e4mii*46i2x4p%=bol13f!q5kk=g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = 'loginhome'
ACCOUNT_LOGOUT_REDIRECT_URL = 'index'
ACCOUNT_LOGOUT_ON_GET = True 
# Application definition

# 세션 데이터를 저장하는 백엔드 설정 
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 86400  # 24시간
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_SECURE = True  # HTTPS 사용 시 True로 변경
SESSION_COOKIE_HTTPONLY = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oreo',
    'rest_framework',
    'django_extensions',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',  # 소셜 계정 지원
    'allauth.socialaccount.providers.kakao',
]

# KaKao Key
SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id': '02e48e6a1120232d96d36976448c4100',
            'secret': 'oInzPJ5NQBGqGWaPqK7Bpib51hXDzsng',
            'key': ''
        }
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # 기본 인증 백엔드
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth 인증 백엔드
]
SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
    
]

ROOT_URLCONF = 'capston.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'oreo', 'Templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'capston.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# 정적 파일 설정
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'oreo', 'static'),
    BASE_DIR / 'oreo' / 'static',
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = BASE_DIR / 'staticfiles'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Kakao OAuth 설정
KAKAO_REST_API_KEY = '02e48e6a1120232d96d36976448c4100'
KAKAO_REDIRECT_URI = "http://127.0.0.1:8000/accounts/kakao/callback/"
KAKAO_AUTH_URL = 'http://kauth.kakao.com/oauth/authorize'
KAKAO_TOKEN_URL = 'http://kauth.kakao.com/oauth/token'
KAKAO_USER_INFO_URL = 'http://kapi.kakao.com/v2/user/me'
KAKAO_CLIENT_SECRET = 'oInzPJ5NQBGqGWaPqK7Bpib51hXDzsng'

# SSL 관련 설정
SECURE_SSL_REDIRECT = False  # 개발 환경에서는 False
SECURE_HSTS_SECONDS = 0      # 개발 환경에서는 0

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.naver.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'xorua4510@naver.com'  # 발신자 이메일 주소
EMAIL_HOST_PASSWORD = 'S8NY1E4R4JVV'  # 이메일 비밀번호
EMAIL_USE_SSL = False  # 이미 EMAIL_USE_TLS가 True로 설정됨


# 로그인 관련 설정 추가
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/loginhome/'
LOGOUT_REDIRECT_URL = '/login/'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'oreo': {  # 앱 이름
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
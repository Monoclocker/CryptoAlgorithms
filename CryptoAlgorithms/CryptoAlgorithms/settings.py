from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Ключ для подписания приложения (без него не запустится)
SECRET_KEY = 'django-insecure-@59u8+e1mvf$g5wq67z06)2+01$@wqn@b+n@14%oc746zb7qz('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-memory',
    }
}


# Компоненты приложения
INSTALLED_APPS = [
    'django.contrib.staticfiles' # для получения статики (CSS, картинки)
]

ROOT_URLCONF = 'CryptoAlgorithms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'CryptoAlgorithms' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'CryptoAlgorithms.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'CryptoAlgorithms' / "static",
]

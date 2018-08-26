"""
Django settings module for buza-website using django-environ.
"""
import os

import dj_database_url
# Configure Django App for Heroku.
import django_heroku
import environ

from buza.settings_base import *  # noqa: F401


env = environ.Env()

# If BASE_DIR is not set, set and create a default for it.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

base_dir = env.path('BASE_DIR', default=BASE_DIR)

DEBUG = env('DJANGO_DEBUG', default=False)
SECRET_KEY = env('DJANGO_SECRET_KEY', default="buza.key")

DATABASES = {
    'default': env.db(
        'DJANGO_DATABASE_URL',
        default=f'sqlite:///' + base_dir('buza.sqlite3'),
    ),
}
if dj_database_url.config():
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)

LANGUAGE_CODE = env('DJANGO_LANGUAGE_CODE', default='en-ZA')
TIME_ZONE = env('DJANGO_TIME_ZONE', default='Africa/Johannesburg')

# Set a few more defaults for development.
os.environ.setdefault('DJANGO_SECRET_KEY', 'buza-website example dev')
os.environ.setdefault('DJANGO_DEBUG', 'True')

# Heroku sets the static and media files urls
django_heroku.settings(locals())

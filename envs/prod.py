"""
Production settings for taskflop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from .dev import *
import dj_database_url


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'www.taskflop.com',
    'taskflop.herokuapp.com',
]

DATABASES['default'] = dj_database_url.config()

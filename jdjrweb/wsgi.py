"""
WSGI config for jdjrweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jdjrweb.settings")

application = get_wsgi_application()

"""


import os

from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))#3
import sys # 4
sys.path.insert(0,PROJECT_DIR) # 5

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jdjrweb.settings")

application = get_wsgi_application()

"""
import os
import sys
import django.core.handlers.wsgi
#from django.conf import settings

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'jdjrweb.settings'

sys.stdout = sys.stderr

DEBUG = True

application = django.core.handlers.wsgi.WSGIHandler()
"""

"""WSGI config for sm_api."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sm_api.settings')

application = get_wsgi_application()

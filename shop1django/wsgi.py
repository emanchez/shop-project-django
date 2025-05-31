"""
WSGI config for shop1django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import environ
from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application

environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop1django.settings')

application = get_wsgi_application()


app = application  # Required for Vercel
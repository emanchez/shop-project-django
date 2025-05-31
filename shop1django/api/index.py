import os
from serverless_wsgi import handle
from django.core.wsgi import get_wsgi_application

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop1django.settings")

# Get Django WSGI application
django_app = get_wsgi_application()

# Convert WSGI app to serverless handler
handler = handle(django_app)  # ← Vercel requires this exact variable name
import environ
from django.core.wsgi import get_wsgi_application
from serverless_wsgi import handle_request

environ.setdefault("DJANGO_SETTINGS_MODULE", "shop1django.settings")

# Initialize Django application
django_app = get_wsgi_application()

# Vercel-required handler function
def handler(event, context):
    return handle_request(django_app, event, context)
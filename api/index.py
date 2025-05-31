from serverless_wsgi import handle_request
from django.core.wsgi import get_wsgi_application
import environ

environ.setdefault("DJANGO_SETTINGS_MODULE", "shop1django.settings")

django_app = get_wsgi_application()

def handler(event, context):
    return handle_request(django_app, event, context)  # Must use this exact signature
import environ
from serverless_wsgi import handle_request
from django.core.wsgi import get_wsgi_application

environ.setdefault("DJANGO_SETTINGS_MODULE", "shop1django.settings")

app = get_wsgi_application()

def handler(event, context):
    return handle_request(app, event, context)  # ← Vercel requires this signature
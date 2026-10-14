import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') # Ya apne project ka settings module name
application = get_wsgi_application()
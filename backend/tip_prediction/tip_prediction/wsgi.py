"""
WSGI config for tip_prediction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'api.deployment_settings'
if 'RENDER_EXTERNAL_AL_HOSTNAME' in os.environ:
    settings_module = 'api.deployment_settings'
else:
    settings_module = 'api.settings'
    

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()

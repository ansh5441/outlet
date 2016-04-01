"""
WSGI config for g project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home/anshuman/projects/g')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "g.settings")

application = get_wsgi_application()

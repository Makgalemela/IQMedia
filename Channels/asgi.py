"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
import channels.asgiref
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Channels.settings")
channel_layer = channels.asgiref.get_channel_layer()
django.setup()
application = get_default_application()

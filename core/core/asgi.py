"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.websocket.routing as chat


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django_asgi_app  = get_asgi_application()


application = ProtocolTypeRouter({
    "http": django_asgi_app ,
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.websocket_urlpatterns
        )
    ),
})
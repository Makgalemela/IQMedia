from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from Echo.consumers import NoseyConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('', NoseyConsumer),
    ])
})
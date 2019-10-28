from django.apps import AppConfig


class EchoConfig(AppConfig):
    name = 'Echo'

    def ready(self):
        from . import signals
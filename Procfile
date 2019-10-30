web: gunicorn Channels.wsgi --log-file -
<<<<<<< HEAD
web1: daphne Channels.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v3
=======
web: daphne Channels.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v3
>>>>>>> e8ab48d794395e18df09eef15f3ed97e27eab569
worker: python manage.py runworker -v3
web: gunicorn Channels.wsgi --log-file -
web1: daphne Channels.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v3
worker: python ./manage.py runworker>>python ./manage.py runworker 2>>./daphneWorker.log >&2&
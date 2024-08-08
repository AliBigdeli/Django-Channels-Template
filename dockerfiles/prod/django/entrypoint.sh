#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput


# Start the server or any other command passed as argument
# echo "Starting server..."
# gunicorn --bind 0.0.0.0:8000 core.wsgi


# echo "Starting ASGI server..."
# python -m gunicorn --bind 0.0.0.0:8000  core.asgi:application -k uvicorn.workers.UvicornWorker 

echo "Starting ASGI server..."
daphne -b 0.0.0.0 -p 8000 core.asgi:application
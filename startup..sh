#!/bin/bash

# Function to start Redis server and store its PID
start_redis() {
    redis-server &
    REDIS_PID=$!
}

# Function to start Celery worker and store its PID
start_celery() {
    uv run celery -A applot worker --loglevel=debug  &
    CELERY_PID=$!
}

# Function to start celery-beat and store its PID
# start_celery_beat() {
#     uv run celery -A applot beat --loglevel=debug --scheduler django_celery_beat.schedulers:DatabaseScheduler  &
#     CELERY_BEAT_PID=$!
# }

# Function to start Django server and store its PID
start_django() {
    uv run manage.py runserver &
    DJANGO_PID=$!
}

# Function to handle shutdown (Ctrl+C)
shutdown() {
    echo "[SHUTDOWN] Shutting down all services..."
    kill $REDIS_PID $CELERY_PID $DJANGO_PID # $CELERY_BEAT_PID
    wait $REDIS_PID $CELERY_PID $DJANGO_PID 2>/dev/null # $CELERY_BEAT_PID 
    echo "[SHUTDOWN] All services have been stopped."
}

# Trap Ctrl+C and call shutdown function
trap shutdown SIGINT

# Start the services
start_redis
start_celery
start_django
start_celery_beat
# Wait for all background processes to finish
wait

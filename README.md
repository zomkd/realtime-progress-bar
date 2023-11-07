# realtime-progress-bar


celery -A main.celery worker --loglevel=info
uvicorn main:app --reload  
redis-server

# Realtime progress bar

Progress bar that shows the task completion status in real time, written using Vue 3, Fast API, Celery, Websockets.


celery -A main.celery worker --loglevel=info
uvicorn main:app --reload  
redis-server


#### Tech Stack:

 - Vue.js (3 version)
 - Fast API
 - Celery
 - Redis
 - Websockets
 - Docker

## Get Started


##### Using Docker

```
git clone git@github.com:zomkd/realtime-progress-bar.git
cd realtime-progress-bar
docker-compose up --build -d
```

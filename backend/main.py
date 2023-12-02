import random
from fastapi.middleware.cors import CORSMiddleware
from celery.result import AsyncResult
from celery import Celery
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from time import sleep
 
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@app.get("/task")
def set_task():
    task = run_task.delay()
    return JSONResponse({"task_id": task.id})

@celery.task(name="run_task", bind=True)
def run_task(self):
    n = 10
    for i in range(0, n):
        sleep(random.randint(1, 5))
        self.update_state(state='PROGRESS', meta={'done': i, 'total': n})
    self.update_state(state='SUCCESS', meta={'done': n, 'total': n})

@app.websocket("/task/{task_id}")
async def task_status_listiner(websocket: WebSocket, task_id: str):
    await websocket.accept()
    task_result = AsyncResult(task_id)

    while task_result.state != 'SUCCESS':
        result = {
            "task_id": task_id,
            "task_status": task_result.state,
            "task_result": task_result.result
        }
        await websocket.send_json(result)
        
    result = {
            "task_id": task_id,
            "task_status": task_result.state,
            "task_result": task_result.result
        }
    await websocket.send_json(result)

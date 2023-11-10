import random
from fastapi.middleware.cors import CORSMiddleware
from celery.result import AsyncResult
from celery import Celery
from fastapi import FastAPI, WebSocket, Body
from fastapi.responses import JSONResponse
from time import sleep
 
app = FastAPI()
origins = [
    "*",
    "http://localhost",
    "http://localhost:5173",
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

@celery.task(name="create_task", bind=True)
def create_task(self, task_name):
    n = 30
    for i in range(0, n):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': n})
        sleep(random.randint(1, 10))
    self.update_state(state='SUCCESS', meta={'done': n, 'total': n})

@app.get("/")
def root():
    return {"msg":"welcome"}


@app.post("/task")
def set_task(payload = Body(...)):
    task_name = payload["task_name"]
    print(task_name)
    task = create_task.delay(task_name)
    return JSONResponse({"task_id": task.id})

@app.websocket("/task/{task_id}")
async def websocket_endpoint(websocket: WebSocket, task_id):
    await websocket.accept()
    task_result = AsyncResult(task_id)
    print(task_result.state)
    running = True
    while running:
        if task_result.state == 'SUCCESS':
            running = False
        if task_result.state == 'PROGRESS':
            result = {
                "task_id": task_id,
                "task_status": task_result.state,
                "task_result": task_result.result
            }
            await websocket.send_json(result)
        else:
            result = {
                "task_id": task_id,
                "task_status": task_result.state,
                "task_result": task_result.result
            }
            await websocket.send_json(result)

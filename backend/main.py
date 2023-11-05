from celery import Celery
from fastapi import FastAPI, WebSocket

app = FastAPI()

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@app.get("/")
def root():
    return {"msg":"welcome"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:

        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"{data}")
        
@celery.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y

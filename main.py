from fastapi import FastAPI
from app.inventory_smart.controller.inventory_controller import router as inventory_router
app = FastAPI()

@app.get("/")
def health():
    return {
        "message" : "Hello world . HEALTH OKAY"
    }

app.include_router(inventory_router)


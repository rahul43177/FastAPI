from fastapi import FastAPI
from .database import engine
from .models import item
from .routers import items

# Create database tables
item.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD App")

# Include routers
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI CRUD App"}

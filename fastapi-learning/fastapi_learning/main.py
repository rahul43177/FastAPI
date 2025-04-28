from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .database import engine
from .models import item
from .routers import items
import time

# Create database tables
item.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI CRUD App",
    description="A simple CRUD application built with FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add request timing middleware
@app.middleware("http")
async def add_timing_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Include routers
app.include_router(items.router)

@app.get("/", 
    response_class=JSONResponse,
    responses={
        200: {
            "description": "Welcome message",
            "content": {
                "application/json": {
                    "example": {"message": "Welcome to FastAPI CRUD App"}
                }
            }
        }
    }
)
def read_root():
    return {"message": "Welcome to FastAPI CRUD App"}

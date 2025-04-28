from fastapi import FastAPI
from routers.itemRouter import router as item_router
from routers.userRouter import router as user_router

app = FastAPI()

app.include_router(user_router , prefix='/api' , tags=['USERS'])
app.include_router(item_router , prefix='/api' , tags = ['ITEMS'])


from fastapi import  FastAPI
from src.routers import user_router 
 
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


app.include_router(user_router.router, prefix="/users") 


from fastapi import  FastAPI
from src.routers import user 
 
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


app.include_router(user.router, prefix="/users") 


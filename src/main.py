from fastapi import FastAPI
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.routers import user
import subprocess
 
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Define a route to trigger the scheduler externally
@app.get("/run-scheduler")
def run_scheduler():
    try:
        subprocess.run(["python", "scripts/scheduler.py"], check=True)
        return {"message": "Scheduler executed successfully."}
    except Exception as e:
        return {"message": f"Scheduler failed: {str(e)}"}

# Include  user router
app.include_router(user.router, prefix="/users")
 


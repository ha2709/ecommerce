from fastapi.testclient import TestClient
<<<<<<< HEAD
from main import app   
=======
from src.main import app  # Replace with the path to your FastAPI app
>>>>>>> main

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

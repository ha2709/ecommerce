from fastapi.testclient import TestClient
from src.main import app  # Replace with the path to your FastAPI app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

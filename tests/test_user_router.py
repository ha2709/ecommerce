import os
import pytest
from httpx import AsyncClient
from main import app   
from dotenv import load_dotenv
import asyncio

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
access_token=""
# Define the headers to be used in the tests
headers = {
    'Accept': 'application/json',
    'Authorization': f"Bearer {access_token}",
    'Content-Type': 'application/json'
    
}

@pytest.yield_fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
 
@pytest.mark.asyncio
async def test_create_user():
    user_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.post("/users/", json=user_data, headers=headers)
    assert response.status_code == 200  # or the expected status code
   

@pytest.mark.asyncio
async def test_verify_user():
    test_token = "test_verification_token"
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get(f"/users/verify/?token={test_token}", headers=headers)
    assert response.status_code in [200, 400]  # Depends on token validity

@pytest.mark.asyncio
async def test_register_user():
    register_data = {
        "email": "newuser@example.com",
        "password": "newpassword123",
        "user_type": "customer",
        "department_id": "1"   
    }
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.post("/users/register/", json=register_data, headers=headers)
    assert response.status_code == 200  #  400 if department doesn't exist
     

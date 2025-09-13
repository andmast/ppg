import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_generate_success():
    response = await AsyncClient(app=app, base_url="http://test").post("/generate", json={"idea": "AI toothbrush"})
    assert response.status_code == 200
    # Expect response to match model structure
    data = response.json()
    assert "idea" in data
    assert "pitch" in data

@pytest.mark.asyncio
async def test_generate_validation():
    response = await AsyncClient(app=app, base_url="http://test").post("/generate", json={})
    assert response.status_code == 422

# More tests to be added for mocking and error handling

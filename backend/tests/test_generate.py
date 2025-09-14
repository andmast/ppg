
import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app

@pytest.mark.asyncio
async def test_generate_success(monkeypatch):
    async def mock_mistral_call(idea):
        return {
            "idea": idea,
            "pitch": f"Mocked pitch for {idea}"
        }
    monkeypatch.setattr("backend.main.call_mistral_api", mock_mistral_call)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/generate", json={"idea": "AI toothbrush"})
    assert response.status_code == 200
    data = response.json()
    assert "idea" in data
    assert "pitch" in data

@pytest.mark.asyncio
async def test_generate_validation():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/generate", json={})
    assert response.status_code == 422


import unittest.mock

@pytest.mark.asyncio
async def test_generate_llm_mock(monkeypatch):
    # Mock the Mistral API call inside the endpoint
    async def mock_mistral_call(idea):
        return {
            "idea": idea,
            "pitch": f"Mocked pitch for {idea}"
        }
    monkeypatch.setattr("backend.main.call_mistral_api", mock_mistral_call)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/generate", json={"idea": "AI toothbrush"})
    assert response.status_code == 200
    data = response.json()
    assert data["pitch"] == "Mocked pitch for AI toothbrush"

@pytest.mark.asyncio
async def test_generate_llm_error(monkeypatch):
    async def mock_mistral_call(idea):
        raise Exception("Mistral API error")
    monkeypatch.setattr("backend.main.call_mistral_api", mock_mistral_call)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/generate", json={"idea": "AI toothbrush"})
    assert response.status_code == 500

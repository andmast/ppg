import os
import httpx

MISTRAL_API_URL = os.getenv("MISTRAL_API_URL", "https://api.mistral.ai/v1/generate")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "your-mistral-api-key")

async def call_mistral_api(idea: str) -> dict:
    if not MISTRAL_API_KEY or MISTRAL_API_KEY == "your-mistral-api-key":
        raise RuntimeError("MISTRAL_API_KEY environment variable not set. Please set a valid API key.")
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": f"Generate a product pitch for: {idea}",
        "max_tokens": 128
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(MISTRAL_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        pitch = data.get("choices", [{}])[0].get("text", "")
        return {"idea": idea, "pitch": pitch}

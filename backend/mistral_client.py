import os
import httpx

MISTRAL_API_URL = os.getenv("MISTRAL_API_URL", "https://api.mistral.ai/v1/chat/completions")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "your-mistral-api-key")

async def call_mistral_api(idea: str) -> dict:
    if not MISTRAL_API_KEY or MISTRAL_API_KEY == "your-mistral-api-key":
        raise RuntimeError("MISTRAL_API_KEY environment variable not set. Please set a valid API key.")
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-large-latest",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates product pitches."},
            {"role": "user", "content": f"Generate a product pitch for: {idea}"}
        ],
        "max_tokens": 128
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(MISTRAL_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        pitch = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        return {"idea": idea, "pitch": pitch}

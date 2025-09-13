

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mistral_client import call_mistral_api

app = FastAPI(title='AI Product Pitch Generator API', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"]
)


class GenerateRequest(BaseModel):
    idea: str

class GenerateResponse(BaseModel):
    idea: str
    pitch: str

@app.post("/generate", response_model=GenerateResponse)
async def generate_pitch(data: GenerateRequest):
    try:
        result = await call_mistral_api(data.idea)
        return GenerateResponse(**result)
    except Exception:
        raise HTTPException(status_code=500, detail="Mistral API error")

@app.get('/health')
def health():
    return {'status': 'ok'}

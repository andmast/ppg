
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.pitch import router as pitch_router

app = FastAPI(title='AI Product Pitch Generator API', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"]
)

@app.get('/health')
def health():
    return {'status': 'ok'}

app.include_router(pitch_router, prefix="/api/v1")

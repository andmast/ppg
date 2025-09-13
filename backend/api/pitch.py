from fastapi import APIRouter
from pydantic import BaseModel

class PitchRequest(BaseModel):
    idea: str

class PitchResponse(BaseModel):
    idea: str
    pitch: str

router = APIRouter()

@router.post("/pitch", response_model=PitchResponse)
def generate_pitch(data: PitchRequest):
    return PitchResponse(
        idea=data.idea,
        pitch=f"Introducing {data.idea}! An innovative solution leveraging AI to transform user experience."
    )

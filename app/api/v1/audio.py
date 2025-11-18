from fastapi import APIRouter, status, Depends, Form, Request
from app.services.utils import get_audio_service, AudioService
from typing import Annotated


router = APIRouter(
    tags=["Speech Generation"],
)

@router.post('/generate_speech')
async def generate_speech(
    language: Annotated[str, Form()],
    voice: Annotated[str, Form()],
    text: Annotated[str, Form()],
    request: Request,
    service: AudioService = Depends(get_audio_service)
):
    import time
    time.sleep(2)  # Simulate processing delay
    audio_url: str = request.url_for("audio_output", path="GCsmZA08oD8.mp3").__str__()
    return {
        "audio_url": audio_url
    }
    
    


@router.get('/languages')
async def get_supported_languages(service: AudioService = Depends(get_audio_service)):
    languages = service.get_supported_languages()
    return {"languages": languages}

@router.get('/voices', status_code=status.HTTP_200_OK)
async def get_supported_voices(gender: str, language: str, service: AudioService = Depends(get_audio_service)):
    print(gender, language)
    voices = service.get_supported_voices(language, gender)
    return {"language": language, "voices": voices}

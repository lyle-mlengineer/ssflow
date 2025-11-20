from fastapi import Security, HTTPException, status
from fastapi import APIRouter, Depends, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.core.config import config
from app.services.utils import get_audio_service, AudioService


templates = Jinja2Templates(directory=config.TEMPLATES_DIR)
   

router = APIRouter(
    tags=["User Interface"],)

@router.get('/', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_landing_page(request: Request):
    """Load the home page"""
    return templates.TemplateResponse(
        "landing_page.html", 
        {
            "request": request,
        }
    )
    
@router.get('/text_to_speech', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_text_to_speech_page(request: Request):
    """Load the text to speech page"""
    service: AudioService = get_audio_service()
    languages = service.get_supported_languages()
    default_language = languages[0] if languages else "en-us"   
    default_voices = service.get_supported_voices(default_language, "female")
    return templates.TemplateResponse(
        "text_to_speech.html", 
        {
            "request": request,
            "title": "SautiFlow TTS",
            "current_page": "tts",
            "languages": languages,
            "default_language": default_language,
            "default_voices": default_voices
        }
    )

@router.get('/audio_picker', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def pick_audio(request: Request):
    """Load the speech to text page"""
    return templates.TemplateResponse(
        "audio_picker.html", 
        {
            "request": request,
            "title": "SautiFlow STT",
            "current_page": "stt"
        }
    )

@router.post('/speech_to_text')
async def get_speech_to_text_page(
    request: Request,
    file: UploadFile = File(...),
    service: AudioService = Depends(get_audio_service)
):
    result = service.save_upload_move_to_drive(file)
    print(result)
    audio_url: str = request.url_for("audio_input", path=result["filename"]).__str__()
    print(audio_url)
    return templates.TemplateResponse(
        "speech_to_text.html", 
        {
            "request": request,
            "title": "SautiFlow STT",
            "current_page": "stt",
            "audio_url": audio_url,
            "fileid": result["file_id"],
        }
    )
    

@router.get('/dashboard', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_dashboard_page(request: Request):
    """Load the dashboard page"""
    return templates.TemplateResponse(
        "dashboard.html", 
        {
            "request": request,
            "title": "SautiFlow Dashboard",
            "current_page": "dashboard"
        }
    )
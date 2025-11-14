from fastapi import Security, HTTPException, status
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.core.config import config


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
    return templates.TemplateResponse(
        "text_to_speech.html", 
        {
            "request": request,
            "title": "SautiFlow TTS",
            "current_page": "tts"
        }
    )
    
@router.get('/speech_to_text', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_speech_to_text_page(request: Request):
    """Load the speech to text page"""
    return templates.TemplateResponse(
        "speech_to_text.html", 
        {
            "request": request,
            "title": "SautiFlow STT",
            "current_page": "stt"
        }
    )
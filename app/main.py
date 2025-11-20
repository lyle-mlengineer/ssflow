from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import config
from app.core.logging import setup_logging
from app.ui.v1 import ui
from app.api.v1.audio import router as audio_router


setup_logging()
app = FastAPI(title=config.APP_NAME, debug=config.DEBUG)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ui.router)
app.include_router(audio_router, prefix="/api/v1/audio")

app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")
app.mount("/audio_output", StaticFiles(directory=config.AUDIO_OUTPUT_DIR), name="audio_output")
app.mount("/audio_input", StaticFiles(directory=config.AUDIO_INPUT_DIR), name="audio_input")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}
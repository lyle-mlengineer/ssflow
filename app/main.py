from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles

from app.core.config import config
from app.core.logging import setup_logging
from app.ui.v1 import ui
from app.api.v1.audio import router as audio_router


setup_logging()
app = FastAPI(title=config.APP_NAME, debug=config.DEBUG)

app.include_router(ui.router)
app.include_router(audio_router, prefix="/api/v1/audio")

app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")
app.mount("/audio_output", StaticFiles(directory=config.AUDIO_OUTPUT_DIR), name="audio_output")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}
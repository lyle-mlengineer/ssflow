from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles

from app.core.config import config
from app.core.logging import setup_logging


setup_logging()
app = FastAPI(title=config.APP_NAME, debug=config.DEBUG)

app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}
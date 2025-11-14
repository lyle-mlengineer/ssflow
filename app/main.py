from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles

from app.core.config import config
from app.core.logging import setup_logging
from app.ui.v1 import ui


setup_logging()
app = FastAPI(title=config.APP_NAME, debug=config.DEBUG)

app.include_router(ui.router)

app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}
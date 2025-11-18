from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    APP_NAME: str = "SautiFlow Labs"
    DEBUG: bool = True

    TEMPLATES_DIR: str = "app/ui/v1/templates"
    STATIC_DIR: str = "app/ui/v1/static"
    
    AUDIO_OUTPUT_DIR: str = "app/api/v1/audio_output"


config = Config()
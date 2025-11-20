from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    APP_NAME: str = "SautiFlow Labs"
    DEBUG: bool = True

    TEMPLATES_DIR: str = "app/ui/v1/templates"
    STATIC_DIR: str = "app/ui/v1/static"
    
    AUDIO_OUTPUT_DIR: str = "app/api/v1/audio_output"
    AUDIO_INPUT_DIR: str = "app/api/v1/audio_input"

    GOOGLE_DRIVE_FOLDER_ID: str = "161MWUwPv6O0wpmCB3Il6wasQ4L0dStOF"
    GOOGLE_DRIVE_CREDENTIALS: str = "/home/lyle/.drive/credentials.json"

    TRANSCRIPTION_API_URL: str = "https://lyle-mlengineer--whisper-transcribe-openai-ssflowtra-90fddf-dev.modal.run"


config = Config()
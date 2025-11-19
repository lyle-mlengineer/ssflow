from typing import LiteralString
import os
from app.core.config import config
from fastapi import UploadFile, File
import shutil


class AudioService:
    def __init__(self):
        pass
    
    def generate_speech(self, text: str, language: str, voice: str) -> str:
        """Generate speech audio from text using specified language and voice."""
        # Placeholder implementation
        audio_path: str = os.path.join(config.AUDIO_OUTPUT_DIR, "raw", "GCsmZA08oD8", "GCsmZA08oD8.mp3")
        return audio_path
    
    def get_supported_languages(self) -> list:
        """Return a list of supported languages for text-to-speech."""
        return ["en-us", "es-es", "fr-fr"]
    
    
    def get_supported_voices(self, language: str, gender: LiteralString = ["male", "female"]) -> list:
        """Return a list of supported voices for a given language."""
        voices = {
            "en-us": {
                "male": ["Bob", "John"],
                "female": ["Alice", "Emily"]
            },
            "es-es": {
                "male": ["Carlos", "Luis"],
                "female": ["Diana", "Maria"]
            },
            "fr-fr": {
                "male": ["Émile", "Paul"],
                "female": ["Sophie", "Julie"]
            }
        }
        return voices.get(language, {}).get(gender, [])
    
    def save_uploaded_file(self, upload_file: UploadFile) -> dict:
        """Save an uploaded file to the specified destination."""
        try:
            # Save the uploaded file
            file_path = os.path.join(config.AUDIO_INPUT_DIR, upload_file.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(upload_file.file, buffer)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            upload_file.file.close()
        return {"filename": upload_file.filename, "content_type": upload_file.content_type}
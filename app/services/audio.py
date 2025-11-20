from typing import LiteralString
import os
from app.core.config import config
from fastapi import UploadFile, File
import shutil
from oryks_google_drive import GoogleDrive
from oryks_google_drive.mime_types import MimeType
import requests


class AudioService:
    def __init__(self):
        self.drive = GoogleDrive()
        self.drive.authenticate_from_credentials(config.GOOGLE_DRIVE_CREDENTIALS)
    
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
        return {"filename": upload_file.filename, "content_type": upload_file.content_type, "file_path": file_path}
    
    def upload_to_google_drive(self, file_path: str) -> str:
        """Upload a file to Google Drive and return the file ID."""
        try:
            file = self.drive.upload_file(
                file_path,
                mime_type=MimeType.AUDIO_MP3.value if file_path.endswith('.mp3') else MimeType.AUDIO_WAV.value
            )
            return file.get("id", "")
        except Exception as e:
            raise RuntimeError(f"Failed to upload file to Google Drive: {e}")
        
    def move_file_in_drive(self, file_id: str, destination_folder_id: str = config.GOOGLE_DRIVE_FOLDER_ID) -> None:
        """Move a file in Google Drive to a different folder."""
        try:
            self.drive.move_file(file_id, destination_folder_id)
        except Exception as e:
            raise RuntimeError(f"Failed to move file in Google Drive: {e}")
        
    def save_upload_move_to_drive(self, upload_file: UploadFile) -> dict:
        """Save an uploaded file and move it to Google Drive."""
        saved_file = self.save_uploaded_file(upload_file)
        file_id = self.upload_to_google_drive(saved_file['file_path'])
        self.move_file_in_drive(file_id)
        
        return {
            "filename": saved_file["filename"],
            "file_id": file_id
        }
    
    def transcribe_audio(self, file_id: str) -> dict:
        """Transcribe the audio file at the given path."""
        response = requests.post(config.TRANSCRIPTION_API_URL, json={"file_id": file_id})
        return response.json()
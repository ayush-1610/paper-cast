from pydantic import BaseSettings

class Settings(BaseSettings):
    MAX_SUMMARY_LENGTH: int = 500
    CHUNK_SIZE: int = 1000
    MAX_KEY_POINTS: int = 5
    MODEL_NAME: str = "sshleifer/distilbart-cnn-12-6"
    
    class Config:
        env_prefix = "PAPERCAST_"

settings = Settings()

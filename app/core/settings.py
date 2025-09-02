import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Lexa AI - Backend"
    PROJECT_VERSION: str = "1.0.0"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SERVER_HOST: str = "http://localhost:8000"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    ALGORITHM: str = "HS256"

settings = Settings()
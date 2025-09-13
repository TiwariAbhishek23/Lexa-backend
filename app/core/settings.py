import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

class Settings:
    PROJECT_NAME: str = "CF0 AI - Backend"
    PROJECT_VERSION: str = "1.0.0"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SERVER_HOST: str = "http://localhost:8000"
    ALGORITHM: str = "HS256"
    OPENAI_API_KEY: str = openai_api_key

settings = Settings()
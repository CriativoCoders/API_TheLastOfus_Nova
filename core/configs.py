from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "sqlite:///database.db"
    SECRET_KEY: str = "chave-secreta"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DB_ECHO: bool = False
    LOG_LEVEL: str = "info"

settings = Settings()
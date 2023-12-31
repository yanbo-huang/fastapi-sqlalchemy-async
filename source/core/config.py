from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

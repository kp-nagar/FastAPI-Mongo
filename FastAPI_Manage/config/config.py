from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str
    MONGO_DB: str
    ADMIN_NAME: str
    ADMIN_EMAIL: str
    ADMIN_PASSWD: str

    class Config:
        env_file = './.env'


settings = Settings()

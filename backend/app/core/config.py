from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = "Argyros"
    DATABASE_URL: str = "postgresql://user:password@host:5432/dbname"
    JWT_SECRET: str = " "

settings = Settings()
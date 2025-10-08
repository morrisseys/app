from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg://controlplane:changeme@db:5432/controlplane"

settings = Settings()
app = FastAPI(title="RMY Controlplane")

@app.get("/health")
def health():
    return {"ok": True}

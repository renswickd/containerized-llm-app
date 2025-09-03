from fastapi import FastAPI
from app.routes import home, ask

app = FastAPI(title="FastAPI Ollama POC")

# Include routers
app.include_router(home.router)
app.include_router(ask.router)

from fastapi import APIRouter, Response, Query
from app.services.ollama_service import generate_response
import json

router = APIRouter()

@router.get("/ask")
def ask(prompt: str):
    result = generate_response(prompt)
    return Response(content=json.dumps(result), media_type="application/json")

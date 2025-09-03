from fastapi import APIRouter, Response, Query
from app.services.ollama_service import generate_response
import json

router = APIRouter()

@router.get("/ask")
def ask(prompt: str):
    try:
        result = generate_response(prompt)
        return Response(content=json.dumps(result), media_type="application/json")
    except Exception as e:
        # logger.error(f"Error occurred while calling the Ollama API: {str(e)}")
        return Response(content=json.dumps({"error": str(e)}), status_code=500, media_type="application/json")
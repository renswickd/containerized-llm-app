import requests
from app.config import OLLAMA_API_URL, OLLAMA_MODEL

def generate_response(prompt: str) -> dict:
    payload = {
        "prompt": prompt,
        "stream": False,
        "model": OLLAMA_MODEL,
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status() 
    return response.json()

def generate_stream_response(prompt: str) -> dict:
    payload = {
        "prompt": prompt,
        "stream": True,
        "model": OLLAMA_MODEL,
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status() 
    return response
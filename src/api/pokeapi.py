import requests
import json
from pathlib import Path

BASE_URL = "https://pokeapi.co/api/v2/"

def fetch_endpoint(endpoint: str) -> dict:
    """GET a PokéAPI endpoint and return JSON."""
    url = BASE_URL + endpoint
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()

def save_json(data: dict, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

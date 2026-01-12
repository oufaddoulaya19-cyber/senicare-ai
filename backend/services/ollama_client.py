import requests
from typing import List, Dict, Any, Optional

OLLAMA_BASE = "http://127.0.0.1:11434"
DEFAULT_MODEL = "llama3.2"

def ollama_chat(
    messages: List[Dict[str, str]],
    model: str = DEFAULT_MODEL,
    temperature: float = 0.4,
    top_p: float = 0.9,
    num_predict: int = 512,
    timeout: int = 120,
) -> str:
    """
    Uses Ollama /api/chat (recommended).
    """
    url = f"{OLLAMA_BASE}/api/chat"
    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": num_predict,
        },
    }
    r = requests.post(url, json=payload, timeout=timeout)
    r.raise_for_status()
    data = r.json()
    # Expected: {"message": {"role":"assistant","content":"..."}}
    return (data.get("message") or {}).get("content", "").strip()

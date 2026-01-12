import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


def _call_ollama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload, timeout=120)

    # Sécurité HTTP
    if r.status_code != 200:
        raise Exception(f"Ollama HTTP error {r.status_code}: {r.text}")

    data = r.json()

    # Cas normal
    if "response" in data:
        return data["response"]

    # Autres formats possibles
    if "message" in data and "content" in data["message"]:
        return data["message"]["content"]

    # Cas erreur Ollama
    if "error" in data:
        raise Exception(f"Ollama error: {data['error']}")

    # Cas inconnu
    raise Exception(f"Unexpected Ollama response: {data}")


def ask_llm(prompt):
    return _call_ollama(prompt)


def analyze_prescription(text):
    prompt = f"""
You are a medical assistant.

The following text comes from OCR of a handwritten medical prescription.
It contains OCR errors.

Your job:
1. Understand the real medications
2. Extract them in clean JSON

Text:
{text}

Return ONLY valid JSON in this format:
{{
  "patient": "",
  "medicaments": [
    {{
      "name": "",
      "dose": "",
      "times": []
    }}
  ]
}}
"""

    return _call_ollama(prompt)

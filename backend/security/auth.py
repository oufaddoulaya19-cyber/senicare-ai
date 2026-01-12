import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("APP_API_KEY", "dev-secret-key")  # change en prod

def require_api_key(x_api_key: str = Header(default=None)):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

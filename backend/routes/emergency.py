from fastapi import APIRouter, Depends
from security.auth import require_api_key
from services.audit_service import log_event

router = APIRouter()

@router.post("/", dependencies=[Depends(require_api_key)])
def emergency_alert(message: str):
    log_event("EMERGENCY_TRIGGERED", {"message": message})
    return {
        "alert": "Alerte reçue",
        "message": message
    }

from fastapi import APIRouter, Depends
from models.reminder_model import MedicationRequest
from services.reminder_service import add_medication, check_reminders
from security.auth import require_api_key
from services.audit_service import log_event

router = APIRouter()

@router.post("/add", dependencies=[Depends(require_api_key)])
def add_med(data: MedicationRequest):
    add_medication(data.name, data.times)
    log_event("MEDICATION_ADDED", {"name": data.name, "times": data.times})

    return {
        "status": "Médicament ajouté",
        "name": data.name,
        "times": data.times
    }

@router.get("/check", dependencies=[Depends(require_api_key)])
def get_reminders():
    reminders = check_reminders()
    log_event("REMINDER_CHECKED", {"count": len(reminders)})

    return {
        "reminders": reminders
    }

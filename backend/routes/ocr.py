from fastapi import APIRouter, UploadFile, File
from services.ocr_service import read_prescription
from services.llm_service import analyze_prescription

router = APIRouter()

@router.post("/")
async def ocr(file: UploadFile = File(...)):
    text = read_prescription(file)

    ai_json = analyze_prescription(text)

    return {
        "raw_text": text,
        "medical": ai_json
    }

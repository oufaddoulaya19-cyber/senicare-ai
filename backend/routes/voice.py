from fastapi import APIRouter, UploadFile, File
from services.voice_service import transcribe_audio
from services.llm_service import ask_llm

router = APIRouter()

@router.post("/")
def voice_input(audio: UploadFile = File(...)):
    # 1. Transcription
    text = transcribe_audio(audio)

    # 2. Envoi au LLM
    response = ask_llm(text)

    return {
        "transcription": text,
        "response": response
    }

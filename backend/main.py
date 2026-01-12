from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat, ocr, auth, reminder, voice, emergency

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(ocr.router, prefix="/ocr")
app.include_router(reminder.router, prefix="/reminder")
app.include_router(voice.router, prefix="/voice")
app.include_router(emergency.router, prefix="/emergency")

@app.get("/")
def root():
    return {"status": "Senior AI Assistant running"}

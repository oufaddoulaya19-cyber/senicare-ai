from openai import OpenAI
import tempfile

client = OpenAI()

def transcribe_audio(audio_file):
    # On sauvegarde temporairement l'audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.file.read())
        tmp_path = tmp.name

    # Transcription avec Whisper
    with open(tmp_path, "rb") as audio:
        transcription = client.audio.transcriptions.create(
            file=audio,
            model="whisper-1"
        )

    return transcription.text

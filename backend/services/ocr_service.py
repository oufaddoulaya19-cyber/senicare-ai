import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import Image
import io

def read_prescription(file):
    image = Image.open(io.BytesIO(file.file.read()))
    text = pytesseract.image_to_string(image)
    
    if not text.strip():
        return "Aucun texte détecté dans l'ordonnance."

    return f"Texte détecté:\n{text}"

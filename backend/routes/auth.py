from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from database import users

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# =========================
# MODELS
# =========================

class RegisterRequest(BaseModel):
    nom: str
    prenom: str
    age: int
    email: EmailStr
    password: str
    maladies: str
    allergies: str
    adresse: str
    emergency_phone: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# =========================
# REGISTER
# =========================
@router.post("/register")
def register(data: RegisterRequest):
    if users.find_one({"email": data.email}):
        return {"error": "Email already exists"}

    password_hash = pwd_context.hash(data.password)

    users.insert_one({
        "nom": data.nom,
        "prenom": data.prenom,
        "age": data.age,
        "email": data.email,
        "password_hash": password_hash,   # ← IMPORTANT
        "maladies": data.maladies,
        "allergies": data.allergies,
        "adresse": data.adresse,
        "emergency_phone": data.emergency_phone
    })

    return {"message": "Account created"}


# =========================
# LOGIN
# =========================
@router.post("/login")
def login(data: LoginRequest):
    user = users.find_one({"email": data.email})

    if not user:
        return {"error": "Invalid credentials"}

    if not pwd_context.verify(data.password, user["password_hash"]):
        return {"error": "Invalid credentials"}

    return {
        "success": True,
        "user_id": str(user["_id"]),
        "prenom": user["prenom"],
        "email": user["email"]
    }

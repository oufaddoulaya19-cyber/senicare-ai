from typing import Tuple

EMERGENCY_KEYWORDS = [
    "douleur poitrine", "douleur thoracique", "difficulté respirer", "essoufflement",
    "perte de connaissance", "convulsion", "paralysie", "avc", "saignement abondant",
    "suic", "overdose", "empoison", "anaphylax", "gonflement visage", "étouff"
]

DOSING_KEYWORDS = [
    "dose", "dosage", "combien mg", "combien de comprimés", "posologie exacte",
    "augmenter", "diminuer", "double dose", "remplacer", "arrêter traitement"
]

def classify_risk(user_text: str) -> Tuple[bool, bool]:
    """
    returns (is_emergency, is_dosing_request)
    """
    t = (user_text or "").lower()
    is_emergency = any(k in t for k in EMERGENCY_KEYWORDS)
    is_dosing = any(k in t for k in DOSING_KEYWORDS)
    return is_emergency, is_dosing

def safety_prefix(is_emergency: bool, is_dosing: bool) -> str:
    if is_emergency:
        return (
            "PRIORITÉ SÉCURITÉ: L’utilisateur décrit possiblement une urgence médicale. "
            "Répondre en conseillant d’appeler immédiatement les urgences locales (112/15/911 selon pays) "
            "ou un proche, et de ne pas attendre. Ne pas donner de diagnostic."
        )
    if is_dosing:
        return (
            "PRIORITÉ SÉCURITÉ: L’utilisateur demande une posologie exacte / modification de traitement. "
            "Refuser de donner une posologie personnalisée. Donner uniquement des conseils généraux sûrs "
            "et recommander de contacter un médecin/pharmacien."
        )
    return (
        "PRIORITÉ SÉCURITÉ: Conseils généraux uniquement. "
        "Ne pas donner de diagnostic certain. "
        "Demander les infos manquantes si nécessaire (âge, symptômes, traitements)."
    )

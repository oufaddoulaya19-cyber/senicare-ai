CRITICAL_KEYWORDS = [
    "aide", "aidez", "mal", "douleur", "tombé", "chute",
    "vertige", "urgence", "je ne me sens pas bien",
    "help", "pain", "fall",
    "ساعد", "ألم", "وقعت", "دوخة"
]

def is_emergency(message: str) -> bool:
    message = message.lower()
    return any(keyword in message for keyword in CRITICAL_KEYWORDS)

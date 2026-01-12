from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# Stockage simple en mémoire (OK pour projet académique)
medications = []

scheduler = BackgroundScheduler()
scheduler.start()

def add_medication(name: str, times: list[str]):
    """
    times = ["08:00", "14:00", "20:00"]
    """
    medications.append({
        "name": name,
        "times": times,
        "last_taken": []
    })

def check_reminders():
    now = datetime.now().strftime("%H:%M")

    reminders = []
    for med in medications:
        if now in med["times"] and now not in med["last_taken"]:
            reminders.append(f"Il est temps de prendre votre médicament {med['name']}.")
            med["last_taken"].append(now)

    return reminders

# Vérifie toutes les minutes
scheduler.add_job(check_reminders, "interval", minutes=1)

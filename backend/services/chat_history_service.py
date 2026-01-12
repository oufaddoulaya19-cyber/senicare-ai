from datetime import datetime
from typing import Optional, List, Dict, Any
from bson import ObjectId

def _now():
    return datetime.utcnow()

def save_chat_message(db, user_id: str, role: str, content: str, meta: Optional[dict] = None) -> str:
    doc = {
        "user_id": user_id,
        "role": role,  # "user" or "assistant" or "system"
        "content": content,
        "meta": meta or {},
        "created_at": _now(),
    }
    res = db["chat_history"].insert_one(doc)
    return str(res.inserted_id)

def get_recent_history(db, user_id: str, limit: int = 20) -> List[Dict[str, Any]]:
    cur = db["chat_history"].find({"user_id": user_id}).sort("created_at", -1).limit(limit)
    items = list(cur)
    items.reverse()
    # normalize ids
    for it in items:
        it["_id"] = str(it["_id"])
    return items

def clear_history(db, user_id: str) -> int:
    res = db["chat_history"].delete_many({"user_id": user_id})
    return res.deleted_count

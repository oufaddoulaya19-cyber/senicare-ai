from pydantic import BaseModel
from typing import List

class MedicationRequest(BaseModel):
    name: str
    times: List[str]

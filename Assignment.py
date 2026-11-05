from dataclasses import dataclass
from datetime import date
import uuid


@dataclass
class Assignment:
    id: int = uuid.uuid4().int
    title: str = ""
    description: str = ""
    subject: str = ""
    due_date: date | None = None
    completed: bool = False

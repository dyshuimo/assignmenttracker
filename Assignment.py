from dataclasses import dataclass
from datetime import date
import uuid
from Subject import Subject


@dataclass
class Assignment:
    id: int = uuid.uuid4().int
    title: str = ""
    description: str = ""
    subject: Subject = Subject(name="")
    due_date: date | None = None
    completed: bool = False

from dataclasses import dataclass, field
from datetime import date
import uuid


@dataclass
class Assignment:
    id: int = field(default_factory=lambda: uuid.uuid4().int)  # generate an uuid
    title: str = ""
    description: str = ""
    subject: str = ""
    due_date: date | None = None
    completed: bool = False

    def __str__(self) -> str:
        return f"""Title: {self.title}
Description: {self.description}
Subject: {self.subject}
Due Date: {self.due_date if self.due_date else "No due date"}
Completed: {"Yes" if self.completed else "No"}"""

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

    def __str__(self) -> str:
        return f"""Assignment ID: {self.id}
Title: {self.title}
Description: {self.description}
Subject: {self.subject}
Due Date: {self.due_date if self.due_date else "No due date"}
Completed: {"Yes" if self.completed else "No"}"""

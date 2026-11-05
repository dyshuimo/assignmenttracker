from datetime import date
import json
from Assignment import Assignment
from Subject import Subject


class DataManager:
    def __init__(self, path):
        self.assignments: list[Assignment] = []
        self.path = path

    @property
    def assignmentsDict(self):
        return [DataManager.objToDict(assignment) for assignment in self.assignments]

    @staticmethod
    def objToDict(obj: Assignment):
        return {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description,
            "subject": {"name": obj.subject.name},
            "due_date": obj.due_date.isoformat() if obj.due_date else None,
            "completed": obj.completed,
        }

    @staticmethod
    def dictToObj(data: dict):
        subject_data = data["subject"]
        subject = Subject(name=subject_data["name"])
        due_date_str = data["due_date"]
        due_date = date.fromisoformat(due_date_str) if due_date_str else None
        return Assignment(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            subject=subject,
            due_date=due_date,
            completed=data["completed"],
        )

    def append(self, data: Assignment):
        if isinstance(data, Assignment):
            self._appendAssignment(data)
        else:
            raise ValueError("Invalid data type. Must be Subject or Assignment.")

    def setAsCompleted(self, index: int):
        if isinstance(index, int) and 0 <= index < len(self.assignments):
            self.assignments[index].completed = True
        else:
            raise ValueError("Invalid data type. Must be Subject or Assignment.")

    def delete(self, index: int):
        if isinstance(index, int) and 0 <= index < len(self.assignments):
            self.assignments.pop(index)
        else:
            raise ValueError("Invalid data type. Must be Subject or Assignment.")

    def _appendAssignment(self, assignment: Assignment):
        self.assignments.append(assignment)

    def _write_to_file(self):
        data = self.assignmentsDict
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)

    def _load_from_file(self):
        try:
            with open(self.path, "r") as file:
                data = json.load(file)
                self.assignments = [DataManager.dictToObj(item) for item in data]
        except Exception:
            self.assignments = []

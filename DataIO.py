from Assignment import Assignment
from datetime import date

"""
Write the file to the disk as assignments.txt
both of my functions receive actual index, so remember to -1 from user input index
"""


class DataManager:
    def __init__(self, path):
        self.assignments: list[Assignment] = []
        self.path = path
        self._readFromFile()

    def read(self):
        try:
            self._readFromFile()
        except Exception as e:
            print(
                f"Error reading from file. The file may be corrupted.\nDetails:\n {e}"
            )
        return self.assignments

    def append(self, data: Assignment):
        if isinstance(data, Assignment):
            self.assignments.append(data)
            self._writeToFile()
        else:
            raise ValueError("Invalid data type. Must be a Assignment.")

    def markCompleted(self, index: int):
        if isinstance(index, int) and 0 <= index < len(self.assignments):
            self.assignments[index].completed = True
        else:
            raise ValueError("Invalid data type. Must be Subject or Assignment.")

    def delete(self, index: int):
        if isinstance(index, int) and 0 <= index < len(self.assignments):
            del self.assignments[index]
        else:
            raise IndexError("Index out of range. Cannot delete assignment.")

    @staticmethod
    def _assignmentToDict(assignment: Assignment) -> dict:
        assignment_dict = {}
        assignment_dict["id"] = assignment.id
        assignment_dict["title"] = assignment.title
        assignment_dict["description"] = assignment.description
        assignment_dict["subject"] = assignment.subject
        assignment_dict["due_date"] = (
            assignment.due_date.isoformat() if assignment.due_date else None
        )
        assignment_dict["completed"] = assignment.completed

        return assignment_dict

    @staticmethod
    def _dictToAssignment(assignment_dict: dict) -> Assignment:
        assignment = Assignment(
            id=int(assignment_dict["id"]),
            title=assignment_dict["title"],
            description=assignment_dict["description"],
            subject=assignment_dict["subject"],
            due_date=date.fromisoformat(assignment_dict["due_date"])
            if assignment_dict["due_date"]
            else None,
            completed=assignment_dict["completed"],
        )
        return assignment

    # for testing only
    def _testMethodClear(self):
        self.assignments.clear()
        self._writeToFile()

    def _assignmentsToString(self) -> list[str]:
        assignments_str = []
        for assignment in self.assignments:
            assignment_dict = DataManager._assignmentToDict(assignment)
            assignments_str.append(str(assignment_dict))
        return assignments_str

    def _stringToAssignments(self, assignments_str: list[str]) -> list[Assignment]:
        assignments_list = []

        for assignment_str in assignments_str:
            try:
                assignment_dict = eval(assignment_str)
                assignment = DataManager._dictToAssignment(assignment_dict)
                assignments_list.append(assignment)
            except Exception:
                continue  # skip

        return assignments_list

    def _writeToFile(self):
        assignments_str = self._assignmentsToString()
        with open(self.path, "w") as file:
            for index, assignment_str in enumerate(assignments_str):
                if index < len(assignments_str) - 1:
                    file.write(assignment_str + "\n")
                else:
                    file.write(assignment_str)

    def _readFromFile(self):
        try:
            with open(self.path, "r") as file:
                assignments_str = file.read().splitlines()
            self.assignments = self._stringToAssignments(assignments_str)
        except FileNotFoundError:
            self.assignments = []

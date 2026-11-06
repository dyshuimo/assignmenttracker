from Assignment import Assignment


class DataManager:
    def __init__(self, path):
        self.assignments: list[Assignment] = []
        self.path = path

    def append(self, data: Assignment):
        pass

    def markCompleted(self, index: int):
        if isinstance(index, int) and 0 <= index < len(self.assignments):
            self.assignments[index].completed = True
        else:
            raise ValueError("Invalid data type. Must be Subject or Assignment.")

    def delete(self, index: int):
        pass

    # should we put conversion in data manager or in assignment?
    @property
    def _dictAssignments(self) -> int:
        return 0

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
            id=assignment_dict["id"],
            title=assignment_dict["title"],
            description=assignment_dict["description"],
            subject=assignment_dict["subject"],
            due_date=assignment_dict["due_date"],
            completed=assignment_dict["completed"],
        )
        return assignment

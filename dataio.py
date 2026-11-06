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

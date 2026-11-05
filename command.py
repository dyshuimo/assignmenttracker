from dataio import DataManager, Assignment, Subject
from datetime import date

data_manager = DataManager("assignments.json")


class CommandLine:
    @staticmethod
    def Menu():
        print("""
            Options:
            1. Add a new assignment
            2. View all assignments
            3. Delete an assignment
            4. Mark an assignment as completed
            5. Exit
            """)

    @staticmethod
    def AddAssignment(data_manager: DataManager):
        title = input("Enter the assignment title: ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")
        subject = input("Enter the subject: ")
        description = input("Enter the assignment description: ")
        assignment = Assignment(
            title=title,
            description=description,
            subject=Subject(name=subject),
            due_date=date.fromisoformat(due_date),
        )
        data_manager.append(assignment)
        data_manager._write_to_file()

    @staticmethod
    def ViewAssignments(data_manager: DataManager):
        data_manager._load_from_file()
        data = data_manager.assignments
        if not data:
            print("Assignments list is empty.")
        else:
            for i, assignment in enumerate(data):
                print(f"Assignment {i + 1}:")
                print(f"Title: {assignment.title}")
                print(f"Due Date: {assignment.due_date}")
                print(f"Subject: {assignment.subject.name}")
                print(f"Description: {assignment.description}")
                print("Completed" if assignment.completed else "Not Completed")
                print("--------------")

    @staticmethod
    def DeleteAssignment(data_manager: DataManager):
        data_manager._load_from_file()
        data = data_manager.assignments
        index = int(input("Enter the number of the assignment to delete: ")) - 1
        if 0 <= index < len(data):
            data_manager.delete(index)
            data_manager._write_to_file()
            print("Assignment deleted.")
        else:
            print("Invalid index. Please try again.")

    @staticmethod
    def MarkAsCompleted(data_manager: DataManager):
        data_manager._load_from_file()
        data = data_manager.assignments
        index = (
            int(input("Enter the number of the assignment to mark as completed: ")) - 1
        )
        if 0 <= index < len(data):
            data_manager.setAsCompleted(index)
            data_manager._write_to_file()
            print("Assignment marked as completed.")
        else:
            print("Invalid index. Please try again.")


def main():
    while True:
        CommandLine.Menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            CommandLine.AddAssignment(data_manager)
        elif choice == "2":
            CommandLine.ViewAssignments(data_manager)
        elif choice == "3":
            CommandLine.DeleteAssignment(data_manager)
        elif choice == "4":
            CommandLine.MarkAsCompleted(data_manager)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

from datetime import date
from Assignment import Assignment
from DataIO import DataManager, FileCorruptedError


def viewAllAssignments(data_manager: DataManager):
    print("\nAssignments:")
    assignments = data_manager.read()

    if len(assignments) == 0:
        print("No assignments saved yet.")
        return

    for index, assignment in enumerate(assignments):
        print(f"Assignment: {index + 1}\n{assignment}\n{overdueStatus(assignment)}\n")


def addAssignment(data_manager: DataManager):
    title = input("Assignment title: ").strip()
    description = input("Description: ").strip()
    subject = input("Subject name: ").strip()
    due = promptDueDate()

    due_date = None
    if due:
        due_date = date.fromisoformat(due.isoformat())

    assignment = Assignment(
        title=title,
        description=description,
        subject=subject,
        due_date=due_date,
        completed=False,
    )

    data_manager.append(assignment)
    print("Assignment added successfully!")


def removeAssignment(data_manager: DataManager):
    viewAllAssignments(data_manager)
    assignments = data_manager.read()
    if assignments:
        try:
            number = int(input("Assignment number to delete: ")) - 1
            data_manager.delete(number)
            print("Assignment deleted.")
        except (
            ValueError
        ):  # this can be deleted after the new DataManager update is merged
            print("Enter a valid assignment number.")
        except IndexError:
            print("Enter a valid assignment number.")


def markAssignmentComplete(data_manager: DataManager):
    viewAllAssignments(data_manager)
    assignments = data_manager.read()
    if assignments:
        try:
            number = int(input("Assignment number to mark complete: ")) - 1
            data_manager.markCompleted(number)
            print("Assignment marked complete.")
        except (
            ValueError
        ):  # this can be deleted after the new DataManager update is merged
            print("Enter a valid assignment number.")
        except IndexError:
            print("Enter a valid assignment number.")


def validateDueDate(input_str: str) -> date | None:
    raw_input = input_str.strip()
    if raw_input == "":
        return None
    try:
        due_date = date.fromisoformat(raw_input)
        return due_date
    except ValueError:
        raise ValueError("Invalid date. Please use format YYYY-MM-DD")


def promptDueDate() -> date | None:
    while True:
        user_text = input("Enter due date (YYYY-MM-DD, press ENTER for NO due date): ")
        try:
            valid_date = validateDueDate(user_text)
            return valid_date
        except ValueError as err:
            print(err)


def isOverdue(assignment: Assignment | None) -> bool:
    due = assignment.due_date if assignment else None
    if due is None:
        return False
    today = date.today()
    return due < today


def overdueStatus(assignment: Assignment) -> str:
    if isOverdue(assignment) and not assignment.completed:
        return "Overdue"
    else:
        return "On time"


def handleCorruptedFile(storagePath: str):
    print("Error reading from file. The file may be corrupted.")
    print("What do you want to do?")
    print("1. Reset the file (this will delete all assignments)")
    print("2. Exit the program")
    choice = input("Choose an option: ")
    if choice == "1":
        DataManager.unsafeWipeFile(storagePath)
    elif choice == "2":
        exit()


def menu():
    print("=== Assignment Tracker ===")
    print("1. Show assignments")
    print("2. Add assignment")
    print("3. Mark assignment complete")
    print("4. Delete assignment")
    print("0. Exit")


def main(storagePath: str = "assignments.txt"):
    while True:
        try:
            manager = DataManager(storagePath)
            break
        except FileCorruptedError:
            handleCorruptedFile(storagePath)

    while True:
        menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                viewAllAssignments(manager)
            elif choice == "2":
                addAssignment(manager)
            elif choice == "3":
                markAssignmentComplete(manager)
            elif choice == "4":
                removeAssignment(manager)
            elif choice == "0":
                break
            else:
                print("Invalid Choice. Choose one of the listed options.")
        except FileCorruptedError:
            handleCorruptedFile(storagePath)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit()

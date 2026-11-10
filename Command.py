from datetime import date
from Assignment import Assignment
from DataIO import DataManager


def view_all_assignments(data_manager: DataManager):
    print("\nAssignments:")
    assignments = data_manager.read()

    if len(assignments) == 0:
        print("No assignments saved yet.")
        return

    for index in range(len(assignments)):
        task = assignments[index]
        task_data = DataManager._assignmentToDict(task)
        print(
            f"\n[{index + 1}] ID:{task_data['id']} | "
            f"Title: {task_data['title']} | Subject: {task_data['subject']}"
        )
        print(
            f"Description: {task_data['description']} | "
            f"Due: {task_data['due_date']}"
        )
        print_assignment_status(task)


def add_assignment(data_manager: DataManager):
    title = input("Assignment title: ").strip()
    description = input("Description: ").strip()
    subject = input("Subject name: ").strip()
    due = prompt_due_date()

    new_id = 1
    assignments = data_manager.read()
    for existing_assignment in assignments:
        if existing_assignment.id >= new_id:
            new_id = existing_assignment.id + 1

    due_date = None
    if due:
        due_date = due.isoformat()

    assignment_data = {
        "id": new_id,
        "title": title,
        "description": description,
        "subject": subject,
        "due_date": due_date,
        "completed": False,
    }
    assignment = DataManager._dictToAssignment(assignment_data)
    data_manager.append(assignment)
    print("Assignment added successfully!")


def remove_assignment(data_manager: DataManager):
    view_all_assignments(data_manager)
    assignments = data_manager.read()
    if assignments:
        try:
            number = int(input("Assignment number to delete: ")) - 1
            data_manager.delete(number)
            data_manager._writeToFile()
            print("Assignment deleted.")
        except ValueError:
            print("Enter a valid assignment number.")
        except IndexError:
            print("Enter a valid assignment number.")


def validate_due_date(input_str: str) -> date | None:
    raw_input = input_str.strip()
    if raw_input == "":
        return None
    try:
        due_date = date.fromisoformat(raw_input)
        return due_date
    except ValueError:
        raise ValueError("Invalid date. Please use format YYYY-MM-DD")

def prompt_due_date() -> date | None:
    while True:
        user_text = input("Enter due date (YYYY-MM-DD, press ENTER for NO due date): ")
        try:
            valid_date = validate_due_date(user_text)
            return valid_date
        except ValueError as err:
            print(err)

def is_overdue(due: date | None) -> bool:
    if due is None:
        return False
    today = date.today()
    return due < today

def get_status_display(is_completed: bool) -> str:
    if is_completed:
        return "Completed"
    else:
        return "Incomplete"

def print_assignment_status(assn: Assignment):
    status_text = get_status_display(assn.completed)
    overdue = is_overdue(assn.due_date)
    print(f"Status: {status_text}", end="")
    if overdue and not assn.completed:
        print(" OVERDUE")
    else:
        print("")

def main():
    manager = DataManager("assignments.txt")

    while True:
        print("=== Assignment Tracker ===")
        print("1. Show assignments")
        print("2. Add assignment")
        print("3. Mark assignment complete")
        print("4. Delete assignment")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_all_assignments(manager)
        if choice == "2":
            add_assignment(manager)
        if choice == "3":
            view_all_assignments(manager)
            assignments = manager.read()
            if assignments:
                try:
                    number = int(input("Assignment number: ")) - 1
                    manager.markCompleted(number)
                    manager._writeToFile()
                    print("Assignment marked complete.")
                except ValueError:
                    print("Enter a valid assignment number.")
                except IndexError:
                    print("Enter a valid assignment number.")
        if choice == "4":
            remove_assignment(manager)
        if choice == "0":
            break
        if choice not in ("0", "1", "2", "3", "4"):
            print("Choose one of the listed options.")

from datetime import date
from Assignment import Assignment
from DataIO import DataManager


def display_assignments(manager):
    print("\nAssignments:")

    try:
        with open("assignments.txt", "r") as file:
            assignments = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        assignments = []

    if not assignments:
        print("No assignments yet.")
        return

    for number, assignment in enumerate(assignments, start=1):
        print(f"{number}. {assignment}")
        
def add_assignment(manager):
    title = input("Title: ")
    subject = input("Subject: ")
    description = input("Description: ")
    due_date_text = input("Due date (YYYY-MM-DD, or leave blank): ")
    if due_date_text:
        try:
            due_date = date.fromisoformat(due_date_text)
        except ValueError:
            print("Enter the date as YYYY-MM-DD.")
            return
    else:
        due_date = None

    assignment = Assignment(
        title=title,
        subject=subject,
        description=description,
        due_date=due_date,
    )
    manager.append(assignment)
    print("Assignment saved.")

def remove_assignment(manager):
    display_assignments(manager)
    if manager.assignments:
        try:
            number = int(input("Assignment number to delete: ")) - 1
            manager.delete(number)
            print("Assignment deleted.")
        except ValueError:
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
            display_assignments(manager)
        elif choice == "2":
            add_assignment(manager)
        elif choice == "3":
            display_assignments(manager)
            if manager.assignments:
                try:
                    number = int(input("Assignment number: ")) - 1
                    manager.markCompleted(number)
                    print("Assignment marked complete.")
                except ValueError:
                    print("Enter a valid assignment number.")
        elif choice == "4":
            remove_assignment(manager)
        elif choice == "0":
            break
        else:
            print("Choose one of the listed options.")
from datetime import date
from Assignment import Assignment
from DataIO import DataManager

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


def add_assignment(data_manager: DataManager):
    title = input("Assignment title: ").strip()
    desc = input("Description: ").strip()
    subject = input("Subject name: ").strip()
    due = prompt_due_date()


    if len(data_manager.assignments) == 0:
        new_id = 1
    else:
        new_id = max(a.id for a in data_manager.assignments) + 1

    new_task = Assignment(
        id=new_id,
        title=title,
        description=desc,
        subject=subject,
        due_date=due,
        completed=False
    )
    data_manager.append(new_task)
    print("Assignment added successfully!")

def view_all_assignments(data_manager: DataManager):
    if len(data_manager.assignments) == 0:
        print("No assignments saved yet.")
        return
    for idx, task in enumerate(data_manager.assignments):
        print(f"\n[{idx+1}] ID:{task.id} | Title: {task.title} | Subject: {task.subject}")
        print(f"Description: {task.description} | Due: {task.due_date}")
        print_assignment_status(task)
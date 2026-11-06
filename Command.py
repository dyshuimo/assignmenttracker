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

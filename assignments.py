from dataio import DataManager, Assignment, Subject
from datetime import date

data_manager = DataManager("assignments.json")

while True:
    print("""
    Options:
    1. Add a new assignment
    2. View all assignments
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
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

    elif choice == "2":
        data_manager._load_from_file()
        data = data_manager.assignments
        for assignment in data:
            print(f"Title: {assignment.title}")
            print(f"Due Date: {assignment.due_date}")
            print(f"Subject: {assignment.subject.name}")
            print(f"Description: {assignment.description}")
            print("--------------")
    else:
        print("Invalid choice. Please try again.")

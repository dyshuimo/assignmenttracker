from dataio import DataManager, Assignment, Subject

if __name__ == "__main__":
    data_manager = DataManager("assignments.json")

    subject = Subject(name="Math")
    assignment = Assignment(
        title="Homework 1", description="Solve problems", subject=subject
    )

    data_manager.append(assignment)

    data_manager._write_to_file()

    for assignment in data_manager.assignments:
        print(
            f"ID: {assignment.id}, Title: {assignment.title}, Subject: {assignment.subject.name}"
        )

from DataIO import DataManager
from Assignment import Assignment
from datetime import date

data_manager = DataManager("assignments.txt")
data_manager._testMethodClear()
assignments = [
    Assignment(
        title="Linear Algebra Problem Set 7",
        description="Questions 1–12 on eigenvalues and diagonalization from Chapter 5.",
        subject="MATH 221",
        due_date=date(2026, 11, 10),
    ),
    Assignment(
        title="Lab Report: Titration",
        description="Write up results from the acid-base titration lab, including error analysis.",
        subject="CHEM 121",
        due_date=date(2026, 11, 13),
        completed=True,
    ),
    Assignment(
        title="Essay Draft",
        description="1500-word argumentative essay on Canadian immigration policy. Submit draft for peer review.",
        subject="POLI 100",
        due_date=date(2026, 11, 18),
    ),
    Assignment(
        title="Binary Search Tree Implementation",
        description="Implement insert, delete, and in-order traversal. Include unit tests.",
        subject="CPSC 221",
        due_date=date(2026, 11, 20),
    ),
    Assignment(
        title="Reading Response 5",
        description="Respond to Chapters 9–10 of the course reader in 500 words.",
        subject="ENGL 110",
        due_date=date(2026, 11, 7),
        completed=True,
    ),
    Assignment(
        title="Group Project Proposal",
        description="One-page proposal outlining topic, team roles, and timeline.",
        subject="COMM 101",
        due_date=date(2026, 11, 25),
    ),
    Assignment(
        title="Kinematics Quiz Prep",
        description="Practice questions for the online quiz on projectile motion.",
        subject="PHYS 117",
        due_date=None,
    ),
    Assignment(
        title="Final Exam Study Guide",
        description="Compile notes from Weeks 1–12 into a study guide.",
        subject="PSYC 101",
        due_date=date(2026, 12, 8),
    ),
]

for assignment in assignments:
    data_manager.append(assignment)

data_manager.markCompleted(0)

for assignment in data_manager.assignments:
    print(
        f"ID: {assignment.id}, Title: {assignment.title}, Subject: {assignment.subject}, Due Date: {assignment.due_date}, Completed: {assignment.completed}"
    )

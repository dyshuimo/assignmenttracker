from DataIO import DataManager
from Assignment import Assignment
from datetime import date
import unittest

STORAGE_PATH = "test_assignments.txt"

DataManager.unsafeWipeFile(STORAGE_PATH)
data_manager = DataManager(STORAGE_PATH)

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


def addTestAssignments(data_manager: DataManager):
    for assignment in assignments:
        data_manager.append(assignment)


def addAndReadAssignments(data_manager: DataManager):
    addTestAssignments(data_manager)
    return data_manager.read()


def isConsistent():
    manager = DataManager(STORAGE_PATH)
    returned_assignments = addAndReadAssignments(manager)
    for assignment in returned_assignments:
        if assignment not in assignments:
            return False
    return True


class Test(unittest.TestCase):
    def testFileSaveAndLoad(self):
        self.assertTrue(isConsistent())

    def testConversion(self):
        self.assertEqual(
            DataManager._assignmentToDict(assignments[0]),
            {
                "id": assignments[0].id,
                "title": "Linear Algebra Problem Set 7",
                "description": "Questions 1–12 on eigenvalues and diagonalization from Chapter 5.",
                "subject": "MATH 221",
                "due_date": "2026-11-10",
                "completed": False,
            },
        )


if __name__ == "__main__":
    unittest.main()

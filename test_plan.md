# Testing Plan

## Overview
**Functions tested:**
Silver: `validateDueDate()`, `isOverdue()`, `overdueStatus()`
Frank: `DataManager.append()`, `DataManager.read()`, `DataManager.delete()`
Alex: `DataManager._assignmentToDict()`, DataManager file save & load persistence
**Testing types:** Unit
**Date:** 2026-11-09

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
| T01 | Test validateDueDate with a valid ISO date string | `"2026-11-08"` | `date(2026, 11, 8)` | Normal | Pass | Silver |
| T02 | Test validateDueDate with an empty input (no due date) | `""` | `None` | Edge | Pass | Silver |
| T03 | Test validateDueDate with date missing leading zero | `"2026-11-8"` | Raise ValueError | Wrong | Pass | Silver |
| T04 | Test isOverdue on an unfinished assignment with a past due date | Assignment(title="HW", description="", subject="Math", due_date=date(2025, 1, 1), completed=False) | `True` | Normal | Pass | Silver |
| T05 | Test overdueStatus for an assignment with no due date | Assignment(title="HW", description="", subject="Math", due_date=None, completed=False) | `"On time"` | Edge | Pass | Silver |
| T06 | Test DataManager append assignment | Initial list: [Assignment("Practice quiz", "25 multiple choices", "Biology")], new assignment: Assignment("Essay", "2000 words essay of comic book", "English") | List length becomes 2, new title is "Essay" | Normal | Pass | Frank |
| T07 | Test DataManager read assignments | Assignment list: [Assignment("Practice quiz", subject="Biology")] | Return the same assignment list | Normal | Pass | Frank |
| T08 | Test DataManager delete assignment at index 0 | List: [Assignment("Practice quiz"), Assignment("Essay")] | List length becomes 1, remaining title is "Essay" | Normal | Pass | Frank |
| T09 | Test save and load assignments from file | Predefined list of 8 sample assignments | Assignments loaded from file match the original list | Normal | Pass | Alex |
| T10 | Test convert Assignment object to dictionary | assignments[0] (Linear Algebra Problem Set 7) | Dictionary with matching id, title, description, subject, due_date iso string, completed flag | Normal | Pass | Alex |

---

## Code Used for Testing
```python
# Automated testing
import unittest
from datetime import date
from Assignment import Assignment
from Command import validateDueDate, isOverdue, overdueStatus
from DataIO import DataManager

# ==============================================
# Alex's tests: Storage, save & load, serialization
# ==============================================
"""Tests for file persistence and Assignment <-> dict conversion."""
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

class AlexStorageTest(unittest.TestCase):
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

# ==============================================
# Silver's tests: Time module (validateDueDate, isOverdue, overdueStatus)
# ==============================================
"""Tests for date validation, overdue checking and status display without interactive input."""
class SilverDateAndStatusTest(unittest.TestCase):
    # Normal: valid date string for validateDueDate
    def test_validateDueDate_normal_valid(self):
        res = validateDueDate("2026-11-08")
        self.assertEqual(res, date(2026, 11, 8))

    # Edge: input is empty, no due date
    def test_validateDueDate_edge_empty(self):
        res = validateDueDate("")
        self.assertEqual(res, None)

    # Wrong: date missing leading zero (2026-11-8 instead of 2026-11-08)
    def test_validateDueDate_wrong_missing_zero(self):
        with self.assertRaises(ValueError):
            validateDueDate("2026-11-8")

    # Normal: unfinished assignment with past due date (isOverdue)
    def test_isOverdue_normal_past(self):
        assign = Assignment(title="HW", description="", subject="Math", due_date=date(2025, 1, 1), completed=False)
        self.assertEqual(isOverdue(assign), True)

    # Edge: assignment with no due date
    def test_overdueStatus_edge_no_due_date(self):
        assign = Assignment(title="HW", description="", subject="Math", due_date=None, completed=False)
        self.assertEqual(overdueStatus(assign), "On time")

# ==============================================
# Frank's tests: Assignment storage, DataManager functions
# ==============================================
"""Tests for assignment storage without interactive input."""
class FrankFunctionTest(unittest.TestCase):
    def test_addAssignment(self):
        assignments = [Assignment(title="Practice quiz", description="25 multiple choices", subject="Biology")]
        data_manager = DataManager("/dev/null")
        data_manager.assignments = assignments
        data_manager._writeToFile = assignments.copy
        assignment = Assignment(title="Essay", description="2000 words essay of comic book", subject="English")
        data_manager.append(assignment)

        self.assertEqual(len(assignments), 2)
        self.assertEqual(assignments[1].title, "Essay")

    def test_readAssignments(self):
        assignments = [Assignment(title="Practice quiz", subject="Biology")]
        data_manager = DataManager("/dev/null")
        data_manager.assignments = assignments
        data_manager._readFromFile = assignments.copy

        self.assertEqual(data_manager.read(), assignments)

    def test_removeAssignment(self):
        assignments = [Assignment(title="Practice quiz", subject="Biology"), Assignment(title="Essay", subject="English")]
        data_manager = DataManager("/dev/null")
        data_manager.assignments = assignments
        data_manager._writeToFile = assignments.copy
        data_manager.delete(0)

        self.assertEqual(len(assignments), 1)
        self.assertEqual(assignments[0].title, "Essay")

if __name__ == '__main__':
    unittest.main()

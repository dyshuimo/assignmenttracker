# Testing Plan

## Overview
**Functions tested:**
Silver: `validateDueDate()`, `isOverdue()`, `overdueStatus()`
Frank: `DataManager.append()`, `DataManager.read()`, `DataManager.delete()`
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

---

## Code Used for Testing
```python
# ==============================================
# Silver's tests: Time module (validateDueDate, isOverdue, overdueStatus)
# ==============================================
"""Tests for date validation, overdue checking and status display without interactive input."""
import unittest
from datetime import date
from Assignment import Assignment
from Command import validateDueDate, isOverdue, overdueStatus

class TestDateAndStatus(unittest.TestCase):
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
from DataIO import DataManager

class TestingFunctions(unittest.TestCase):
    def test_addAssignment(self):
        assignments = [Assignment(title="Practice quiz", description= "25 multiple choices" ,subject="Biology")]
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

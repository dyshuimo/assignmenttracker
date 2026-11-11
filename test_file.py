# #Automated testing

# import unittest

# def your_function_here(param):
#     pass #placeholder

# class TestYourFunction(unittest.TestCase):

#     # ADD TESTS HERE
#     # NOTE: use self.assertTrue, self.assertFalse or self.assertEqual
#     pass #placeholder

# if __name__ == '__main__':
#     unittest.main()


# Automated testing
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

    # Wrong: wrong date format
    def test_validateDueDate_wrong_format(self):
        with self.assertRaises(ValueError):
            validateDueDate("12/20/2026")

    # Normal: unfinished assignment with past due date (isOverdue)
    def test_isOverdue_normal_past(self):
        assign = Assignment(title="HW", description="", subject="Math", due_date=date(2025, 1, 1), completed=False)
        self.assertEqual(isOverdue(assign), True)

    # Edge: assignment with no due date
    def test_overdueStatus_edge_no_due_date(self):
        assign = Assignment(title="HW", description="", subject="Math", due_date=None, completed=False)
        self.assertEqual(overdueStatus(assign), "On time")

if __name__ == '__main__':
    unittest.main()
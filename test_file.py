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
    # Test validateDueDate
    def test_validateDueDate_normal_valid(self):
        res = validateDueDate("2026-11-08")
        self.assertEqual(res, date(2026, 11, 8))

    def test_validateDueDate_edge_empty_input(self):
        res = validateDueDate("")
        self.assertEqual(res, None)

    def test_validateDueDate_error_wrong_format(self):
        with self.assertRaises(ValueError):
            validateDueDate("12/20/2026")


# Test isOverdue
    def test_isOverdue_future_date(self):
        due_date = date(2026, 11, 8)
        self.assertAlmostEqual(isOverdue(due_date), False)

    def test_isOverdue_past_date(self):
        due_date = date(2020, 11, 8)
        self.assertAlmostEqual(isOverdue(due_date), True)

    def test_isOverdue_today(self):
        due_date = date.today()
        self.assertAlmostEqual(isOverdue(due_date), False)
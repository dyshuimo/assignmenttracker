"""Tests for assignment storage without interactive input."""

import unittest

from Assignment import Assignment
from DataIO import DataManager


class TestingFunctions(unittest.TestCase):
    def test_addAssignment(self):
        assignments = [Assignment(title="Practice quiz", description= "25 multiple choices" ,subject="Biology")]
        data_manager = DataManager("/dev/null")
        data_manager.assignments = assignments
        data_manager._writeToFile = assignments.copy
        assignment = Assignment(title="Essay", description="2000 words esaay of comic book", subject="English")
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


if __name__ == "__main__":
    unittest.main()

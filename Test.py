### Manual Tests

from Assignment import Assignment
from datetime import date
from DataIO import DataManager

# validate uuid's uniqueness
assignment1 = Assignment(title="Assignment 1")
assignment2 = Assignment(title="Assignment 2")
print(assignment1.id != assignment2.id)


a = Assignment(title="HW1", due_date=date(2026, 11, 20), completed=True)
# check string
print(a)

manager = DataManager("assignments_test.txt")
manager.append(a)
# wrong index
manager.delete(-99)

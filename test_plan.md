# Testing Plan

## Overview
**Functions tested: Assignment.__init__ **  
**Testing types:** Unit / Integration / Regression  
**Date:**  
Nov 13

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
| T01 | test uuid uniqueness | `Assignment(title="Assignment 1")`, `Assignment(title="Assignment 2")` | `True` | Normal | Passed ||
| T02 | __str__ of assignment  | `Assignment(title="HW1", due_date=date(2026, 11, 20), completed=True)` | `Title: HW1`<br>`Description: `<br>`Subject: `<br>`Due Date: 2026-11-20`<br>`Completed: Yes` | Normal | Passed | |
| T03 | wrong index for delete() | `manager.delete(-99)` | IndexError | Error | Passed |  |
---

## Code Used for Testing

```python
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
```

# Testing Plan

## Overview
**Functions tested:**  `validateDueDate()`, `isOverdue()`, `overdueStatus()`
**Testing types:** Unit 
**Date:**  2026-11-09

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
| T01 | Test validateDueDate with a valid ISO date string | `"2026-11-08"` | `date(2026, 11, 8) | Normal | Silver |
| T02 | Test validateDueDate with an empty input(no due date) | `""` | `None` | Edge | Silver |
| T03 | Test validateDueDate with date missing leading zero | `"2026-11-8"` | Raise ValueError | Wrong | Silver |
| T04 | Test isOverdue on an unfinished assignment with a past due date | Assignment(title="HW", description="", subject="Math", due_date=date(2025, 1, 1), completed=False) | `True` | Normal | Silver |
| T05 | Test overdueStatus for an assignment with no due date | Assignment(title="HW", description="", subject="Math", due_date=None, completed=False) | `"On time"` | Edge | Silver |
---

---

## Code Used for Testing

```python
# Paste your Python test script here


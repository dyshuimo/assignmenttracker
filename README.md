# Assignment Tracker Program

## Description
This proogram is made for high school students to manage their assiments.

Users can add new assignments, view all saved assignments, view assignments sorted by subject, mark assignments as completed/incomplete, and delete assignments.

The program could check the due date and tells users whether an assignment is overdue or not, and all assignments data is saved into file `assigments.txt`, so informations could stay after close the program.

## How to Run

1. Download all files from the repository
2. Open the repository in VSCode
3. Make sure the program needs to be running in the latest Python version
4. Open **main.py**
5. Run main.py
6. Follow the prompts in the terminal

### Silver's Example: Show assignment

Input:
Choose an option: 1

Output:

Assignments:
Assignment: 1
Title: Math Homework
Description: Page 20 questions
Subject: Math
Due Date: 2026-11-15
Completed: No
Overdue

Assignment: 2
Title: ICS Project
Description: Finish README
Subject: Computer Science
Due Date: 2026-11-20
Completed: Yes
On time

### Frank's Example: Delete Task

```bash
Assignments:
Assignment: 1
Title: Math worksheegt
Description: Practice for derivatives
Subject: MCV4U
Due Date: 2026-10-23
Completed: No
Overdue
```

Input:

```bash
Assignment number to delete: 1
```

Output:

```bash
Assignment deleted.

### Alex's example: Add assignment

Input
Choose option 2 in the menu.
```bash
Choose an option: 2
```

The program will prompt you for the assignment title

Example input: 
```bash
Assignment title: Unit 3 Essay
```

And other details like description, subject, and due date. 
```bash
Description: Write an essay about the main themes of Unit 3
Subject name: English
Enter due date (YYYY-MM-DD, press ENTER for NO due date): 2026-11-08
```

Output
```bash
Assignment added successfully!
```

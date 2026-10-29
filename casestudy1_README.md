# Student Timetable Conflict Detection

## Project Description
The Student Timetable Conflict Detection system is a Python program that checks a timetable for room conflicts. It compares subjects scheduled on the same day and period to identify whether two subjects are assigned to the same room at the same time.

## Objectives
- To detect room conflicts in a timetable.
- To compare subjects based on day and period.
- To identify subjects assigned to the same room at the same time.
- To display conflict details clearly.

## Technologies Used
- **Programming Language:** Python
- **Concepts:** Lists, Tuples, Nested Loops, Conditional Statements

## How the Program Works
1. The timetable is stored as a list of tuples.
2. Each tuple contains the subject name, day, period, and room number.
3. Nested loops compare each pair of timetable entries.
4. If two subjects have the same day and period, their room numbers are checked.
5. If the room numbers are the same, a room conflict is reported.
6. Otherwise, the program displays that there is no room conflict between those subjects.
7. Finally, the program displays a completion message.

## Sample Input
```python
timetable = [
    ("Python", "Monday", 1, "R101"),
    ("Maths", "Monday", 2, "R102"),
    ("Web", "Monday", 1, "R103"),
    ("English", "Tuesday", 1, "R101"),
    ("AI", "Monday", 1, "R101")
]
```

## Sample Output
```text
No room conflict between Python and Web
Room conflict detected
Subjects: Python and AI
Day: Monday
Period: 1
Room: R101
No room conflict between Web and AI
Timetable checking completed
```

## Advantages
- Simple and easy to understand.
- Detects room conflicts automatically.
- Reduces manual timetable-checking effort.
- Displays the subjects, day, period, and room involved in a conflict.

## Limitations
- The timetable data must be entered manually.
- The program checks room conflicts only.
- It does not detect teacher or student scheduling conflicts.

## How to Run
1. Install Python on your computer.
2. Save the code in a file named `timetable_conflict.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

```bash
python timetable_conflict.py
```

## Conclusion
This project demonstrates how Python can be used to detect room conflicts in a timetable using lists, tuples, nested loops, and conditional statements. It helps make timetable checking simpler and more efficient.

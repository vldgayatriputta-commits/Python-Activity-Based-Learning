# Examination Result and Grace-Mark Validation

## Overview
The **Examination Result and Grace-Mark Validation** is a Python program that processes student marks, determines pass or fail status, and calculates overall examination statistics. It identifies the highest and lowest marks and computes the average marks for all students.

**Note:** The current implementation checks a fixed pass mark of 50. It does not yet implement grace marks, subject-wise criteria, or maximum-mark validation.

## Features
- Stores student names and marks using Python lists.
- Calculates total marks.
- Determines the highest and lowest marks.
- Calculates average marks.
- Classifies students as Pass or Fail.
- Displays individual results and overall statistics.

## Requirements
- Python 3.x
- No external libraries required.

## Input Details
- `students`: List containing student names.
- `marks`: List containing the corresponding marks of each student.
- Pass mark: 50.

Each student's name corresponds to the mark at the same index in the `marks` list.

## How It Works
1. The program initializes the student names and marks.
2. It initializes variables to calculate the total, highest, and lowest marks.
3. A loop processes each student.
4. The student's marks are added to the total.
5. Conditional statements update the highest and lowest marks.
6. Each student is classified as Pass if their marks are at least 50; otherwise, they are classified as Fail.
7. After processing all students, the program calculates and displays the average, total, highest, and lowest marks.

## Source Code
Save the Python program as `examination_result.py`.

```python
students = ["Asha", "Balu", "Charan", "Divya"]
marks = [85, 45, 92, 68]

total = 0
highest = marks[0]
lowest = marks[0]

for i in range(len(students)):
    total = total + marks[i]

    if marks[i] > highest:
        highest = marks[i]

    if marks[i] < lowest:
        lowest = marks[i]

    print("Student:", students[i])
    print("Marks:", marks[i])

    if marks[i] >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print()

average = total / len(marks)

print("Total marks:", total)
print("Average marks:", round(average, 2))
print("Highest marks:", highest)
print("Lowest marks:", lowest)
```

## How to Run
1. Install Python 3 if necessary.
2. Save the code as `examination_result.py`.
3. Open a terminal or command prompt in the project folder.
4. Run the command:

```bash
python examination_result.py
```

On some systems, use `python3 examination_result.py`.

## Sample Output

```text
Student: Asha
Marks: 85
Result: Pass

Student: Balu
Marks: 45
Result: Fail

Student: Charan
Marks: 92
Result: Pass

Student: Divya
Marks: 68
Result: Pass

Total marks: 290
Average marks: 72.5
Highest marks: 92
Lowest marks: 45
```

## Customization
- Add more students to the `students` list.
- Add the corresponding marks to the `marks` list.
- Change the pass mark by modifying the condition `marks[i] >= 50`.
- Ensure both lists contain the same number of elements.

## Limitations
- The program handles one
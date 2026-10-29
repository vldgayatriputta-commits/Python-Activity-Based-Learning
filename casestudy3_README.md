# Student Group Formation with Score Balancing

## Project Description
This Python program divides students into two groups while attempting to balance their total scores. Each student's score is added to the group that currently has the lower or equal total.

## Objectives
- To divide students into two groups.
- To distribute scores using a simple balancing rule.
- To calculate the total score of each group.
- To find the difference between the two group totals.

## Technologies Used
- **Programming Language:** Python
- **Concepts:** Lists, Loops, Conditional Statements, `append()`, Arithmetic Operations

## How the Program Works
1. The student names and their scores are stored in two lists.
2. Two empty lists are created to store the students in each group.
3. The total score of each group starts at zero.
4. The program checks the group totals for each student.
5. If Group 1's total is less than or equal to Group 2's total, the student is added to Group 1. Otherwise, the student is added to Group 2.
6. The program updates the selected group's total score.
7. It displays the students and total score in each group.
8. Finally, it calculates and displays the absolute difference between the group totals.

## Sample Input
```python
students = ["Asha", "Balu", "Charan", "Divya", "Esha", "Farhan"]
scores = [90, 75, 85, 60, 80, 70]
```

## Sample Output
```text
Group 1: ['Asha', 'Charan', 'Esha']
Group 1 total: 255
Group 2: ['Balu', 'Divya', 'Farhan']
Group 2 total: 205
Difference between groups: 50
```

## Advantages
- Easy to understand and implement.
- Automatically assigns students based on current group totals.
- Helps demonstrate a basic score-balancing approach.

## Limitations
- The program uses a simple greedy method and does not guarantee the smallest possible difference.
- Students are assigned in the order they appear in the list.
- It balances total scores only; it does not consider other student characteristics.

## How to Run
1. Install Python on your computer.
2. Save the code in a file named `student_group_balancing.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

```bash
python student_group_balancing.py
```

## Conclusion
This project demonstrates how Python lists, loops, and conditional statements can be used to divide students into two groups based on their scores and compare the groups' total scores.

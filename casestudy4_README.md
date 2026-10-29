# Water Distribution Fairness Analysis

## Project Description
This Python program analyzes water demand and supply across different areas. For each area, it calculates the total supply, total demand across the listed supply entries, average supply, and shortage. It then labels the area as underserved or as having sufficient supply based on the calculated shortage.

## Objectives
- To calculate total water supply for each area.
- To calculate total demand using the demand value and number of supply entries.
- To find the average supply.
- To calculate shortages and display a supply status for each area.

## Technologies Used
- **Programming Language:** Python
- **Concepts:** Lists, Nested Lists, Loops, Conditional Statements, Arithmetic Operations, `round()`

## How the Program Works
1. The area names and demand values are stored in lists.
2. The supply values for each area are stored in a nested list.
3. The outer loop processes each area.
4. The inner loop adds the supply values for that area.
5. Total demand is calculated by multiplying the area's demand value by the number of supply entries.
6. The program calculates average supply and shortage.
7. If the shortage is greater than zero, the area is marked as **Underserved**; otherwise, it is marked as **Sufficient supply**.
8. The results are printed for each area.

## Sample Input
```python
areas = ["Area A", "Area B", "Area C"]
demand = [100, 120, 80]

supply = [
    [90, 80, 100],
    [70, 90, 60],
    [80, 75, 80]
]
```

## Sample Output
```text
Area: Area A
Total demand: 300
Total supply: 270
Average supply: 90.0
Shortage: 30
Status: Underserved

Area: Area B
Total demand: 360
Total supply: 220
Average supply: 73.33
Shortage: 140
Status: Underserved

Area: Area C
Total demand: 240
Total supply: 235
Average supply: 78.33
Shortage: 5
Status: Underserved
```

## Advantages
- Makes it easy to compare supply levels across areas.
- Calculates totals, averages, and shortages automatically.
- Uses simple Python concepts suitable for beginners.

## Limitations
- The program uses sample data entered directly in the code.
- It assumes each area's demand value applies to every supply entry in that area's list.
- It marks a status based only on the calculated shortage.

## How to Run
1. Install Python on your computer.
2. Save the code in a file named `water_distribution_analysis.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

```bash
python water_distribution_analysis.py
```

## Conclusion
This project demonstrates how Python can be used to compare water demand and supply across areas, calculate shortages, and identify areas that may need additional water resources.

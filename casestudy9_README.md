# Disaster Relief Supply Allocation

## Overview
The **Disaster Relief Supply Allocation** is a Python program that distributes limited relief supplies among different areas according to their priority levels. It calculates allocated supplies, unmet demand, and remaining stock.

## Features
- Stores area names, required quantities, and priority levels.
- Sorts areas according to priority, from highest to lowest.
- Allocates limited supplies based on priority.
- Calculates unmet demand for each area.
- Displays the remaining stock after allocation.

## Requirements
- Python 3.x
- No external libraries required.

## Input Details
- `areas`: Names of the areas requiring supplies.
- `required`: Supply quantity required by each area.
- `priority`: Priority score for each area. Higher values indicate higher priority.
- `stock`: Total available supply, set to `200` in this example.

## Working Procedure
1. The program sorts areas according to their priority scores.
2. The corresponding requirements and area names are swapped together to maintain correct associations.
3. Supplies are allocated to the highest-priority area first.
4. If the remaining stock cannot satisfy an area's full requirement, all remaining stock is allocated to that area.
5. Unmet demand is calculated by subtracting allocated supplies from required supplies.
6. The program displays the allocation details and remaining stock.

## Sample Output

```text
Area: Area A
Required: 100
Allocated: 100
Unmet demand: 0

Area: Area C
Required: 60
Allocated: 60
Unmet demand: 0

Area: Area B
Required: 80
Allocated: 40
Unmet demand: 40

Area: Area D
Required: 50
Allocated: 0
Unmet demand: 50

Remaining stock: 0
```

## How to Run
1. Install Python 3 on your computer.
2. Save the Python code in a file named `disaster_relief_allocation.py`.
3. Open a terminal or command prompt in the project folder.
4. Run the following command:

```bash
python disaster_relief_allocation.py
```

On some systems, use `python3` instead of `python`.

## Customization
- Add or remove areas by updating the `areas`, `required`, and `priority` lists.
- Change `stock` to represent the available supply.
- Adjust priority scores according to the relief allocation policy.
- Ensure all three lists have the same number of elements.

## Important Notes
- Higher priority scores are served first.
- Areas with equal priority retain their original relative order in this example.
- Supplies are allocated sequentially rather than proportionally.
- If supplies run out, subsequent areas may receive no supplies.
- The program assumes all supplies are interchangeable. Real-world disaster relief may require separate allocation plans for food, water, medicines, and other essential items.

## Conclusion
This program demonstrates how Python lists, nested loops, conditional statements, and sorting logic can be used to manage limited resources and prioritize urgent needs during disaster relief operations.

# Food Supply Chain Stock Reconciliation

## Project Description
This Python program checks stock records for different locations. It calculates the expected remaining stock by subtracting the distributed and damaged quantities from the received quantity. It compares the calculated stock with the recorded stock, reports any discrepancy, and checks whether replenishment is required.

## Objectives
- To calculate the expected remaining stock at each location.
- To compare calculated stock with recorded stock.
- To identify and report stock discrepancies.
- To determine whether replenishment is required when recorded stock is below 100 units.

## Technologies Used
- **Programming Language:** Python
- **Concepts:** Lists, Loops, Conditional Statements, Arithmetic Operations

## How the Program Works
1. Location names and stock details are stored in separate lists.
2. The program processes each location using a loop.
3. It calculates stock using: received quantity − distributed quantity − damaged quantity.
4. It compares the calculated stock with the recorded stock.
5. If both values match, it displays `Stock matches`; otherwise, it reports a discrepancy and its difference.
6. If recorded stock is below 100 units, the program calculates how many units are needed to reach 100. Otherwise, it reports that replenishment is not required.
7. The results are displayed for every location.

## Sample Input
```python
locations = ["Location A", "Location B", "Location C"]
received = [500, 400, 300]
distributed = [350, 250, 200]
damaged = [20, 30, 10]
remaining = [120, 100, 90]
```

## Sample Output
```text
Location: Location A
Received: 500
Distributed: 350
Damaged: 20
Recorded stock: 120
Calculated stock: 130
Status: Discrepancy detected
Difference: 10
Replenishment not required

Location: Location B
Received: 400
Distributed: 250
Damaged: 30
Recorded stock: 100
Calculated stock: 120
Status: Discrepancy detected
Difference: 20
Replenishment not required

Location: Location C
Received: 300
Distributed: 200
Damaged: 10
Recorded stock: 90
Calculated stock: 90
Status: Stock matches
Replenishment required: 10
```

## Advantages
- Helps identify differences between expected and recorded stock.
- Calculates stock discrepancies automatically.
- Flags locations that may need replenishment.
- Uses simple Python concepts suitable for beginners.

## Limitations
- The stock values are entered manually in the program.
- The replenishment check uses a fixed minimum stock level of 100 units.
- It does not automatically update inventory records or place orders.

## How to Run
1. Install Python on your computer.
2. Save the code in a file named `food_supply_stock_reconciliation.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

```bash
python food_supply_stock_reconciliation.py
```

## Conclusion
This project demonstrates how Python can be used to reconcile inventory records, detect stock discrepancies, and identify locations that require replenishment.

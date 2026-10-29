# Multi-Route Courier Dispatch Planning

## Project Description
This Python program assigns packages to vehicles based on their weight and the available vehicle capacity. It checks each vehicle in order and assigns a package to the first vehicle that can carry it without exceeding its capacity. If no vehicle has enough remaining capacity, the package is marked as unable to be dispatched.

## Objectives
- To assign packages to available vehicles.
- To ensure vehicle capacity limits are not exceeded.
- To display each package's priority and assigned vehicle.
- To report packages that cannot be dispatched.
- To display the final load of each vehicle.

## Technologies Used
- **Programming Language:** Python
- **Concepts:** Lists, Tuples, Loops, Conditional Statements, Variables, Boolean Values

## How the Program Works
1. Package details are stored as tuples containing the package ID, weight, and priority.
2. The `capacity` list stores the maximum capacity of each vehicle.
3. The `load` list tracks the current load of each vehicle.
4. For each package, the program checks vehicles one by one.
5. If a vehicle has enough remaining capacity, the package is assigned to that vehicle and its load is updated.
6. If no vehicle can accept the package, the program displays that it cannot be dispatched.
7. At the end, the program displays the total load assigned to each vehicle.

## Sample Input
```python
packages = [
    ("P101", 8, "Urgent"),
    ("P103", 6, "Urgent"),
    ("P105", 10, "Urgent"),
    ("P102", 12, "Normal"),
    ("P104", 15, "Normal")
]

capacity = [20, 25]
```

## Sample Output
```text
Package: P101
Priority: Urgent
Assigned to Vehicle 1

Package: P103
Priority: Urgent
Assigned to Vehicle 1

Package: P105
Priority: Urgent
Assigned to Vehicle 2

Package: P102
Priority: Normal
Assigned to Vehicle 2

Package: P104
Status: Cannot be dispatched

Vehicle 1 load: 14
Vehicle 2 load: 22
```

## Advantages
- Simple way to assign packages based on available capacity.
- Prevents a vehicle from exceeding its maximum load.
- Displays dispatch status clearly for each package.

## Limitations
- Vehicles are checked in list order, so the program may not find the best possible assignment.
- Although package priority is displayed, it does not affect assignment order.
- The program considers weight capacity only; it does not plan actual delivery routes.

## How to Run
1. Install Python on your computer.
2. Save the code in a file named `courier_dispatch.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

```bash
python courier_dispatch.py
```

## Conclusion
This project demonstrates a basic courier dispatch planning approach using Python. It assigns packages to vehicles while respecting their capacity limits and reports packages that cannot be accommodated.

# Environmental Monitoring Data Analyzer

## Overview
The **Environmental Monitoring Data Analyzer** is a Python program that analyzes air-quality or water-quality readings collected at multiple locations. It calculates the average, highest, and lowest reading for each location and checks whether the highest reading exceeds a user-defined limit.

## Features
- Stores location names and their readings in nested lists.
- Calculates the average reading for each location.
- Finds the highest and lowest readings for each location.
- Classifies each location as **Limit exceeded** or **Within limit**.
- Displays results in a clear, readable format.

## Requirements
- Python 3.x
- No external libraries are required.

## How It Works
1. `locations` contains the names of the monitoring locations.
2. `readings` contains a list of measurements for each location. Each inner list corresponds to the location at the same index in `locations`.
3. `limit` sets the threshold value (`60` in this example).
4. The outer loop processes each location.
5. The inner loop calculates the total and identifies the highest and lowest readings.
6. The program calculates the average and prints the statistics.
7. If the highest reading is greater than the limit, the location is marked **Limit exceeded**. Otherwise, it is marked **Within limit**.

## Code
Save the Python program in a file named `environmental_monitor.py`.

```python
locations = ["College Gate", "Library", "Laboratory"]

readings = [
    [45, 50, 55],
    [30, 35, 40],
    [75, 85, 90]
]

limit = 60

for i in range(len(locations)):
    total = 0
    highest = readings[i][0]
    lowest = readings[i][0]

    for j in range(len(readings[i])):
        value = readings[i][j]
        total = total + value

        if value > highest:
            highest = value

        if value < lowest:
            lowest = value

    average = total / len(readings[i])

    print("Location:", locations[i])
    print("Average reading:", round(average, 2))
    print("Highest reading:", highest)
    print("Lowest reading:", lowest)

    if highest > limit:
        print("Status: Limit exceeded")
    else:
        print("Status: Within limit")

    print()
```

## How to Run
1. Install Python 3 if it is not already installed.
2. Save the code as `environmental_monitor.py`.
3. Open a terminal or command prompt in the folder containing the file.
4. Run:

```bash
python environmental_monitor.py
```

On some systems, use `python3 environmental_monitor.py`.

## Sample Output

```text
Location: College Gate
Average reading: 50.0
Highest reading: 55
Lowest reading: 45
Status: Within limit

Location: Library
Average reading: 35.0
Highest reading: 40
Lowest reading: 30
Status: Within limit

Location: Laboratory
Average reading: 83.33
Highest reading: 90
Lowest reading: 75
Status: Limit exceeded
```

## Customization
- Add or rename locations in the `locations` list.
- Add the corresponding measurements to `readings`.
- Change `limit` to use a different threshold.
- Ensure each location has at least one reading and that `locations` and `readings` have matching lengths.

## Note
This example compares the **highest reading** at each location with the threshold. A location is marked **Limit exceeded** only when its highest reading is strictly greater than `limit`; a reading equal to the limit is treated as within the limit.

The threshold value and units should be selected according to the pollutant or water-quality measure being monitored.

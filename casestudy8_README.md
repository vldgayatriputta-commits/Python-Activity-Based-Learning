# Integrated Campus Energy and Water Audit

## Overview
The **Integrated Campus Energy and Water Audit** is a Python program that analyzes electricity and water consumption across multiple campus buildings over several days. It calculates consumption totals and costs, measures the percentage change in electricity usage, flags buildings whose total cost exceeds a specified limit, and ranks buildings by total cost.

## Features
- Tracks electricity and water readings for each building.
- Calculates total electricity and water consumption.
- Calculates electricity cost, water cost, and combined cost.
- Calculates percentage change in electricity usage from the first reading to the last reading.
- Classifies each building as **Excessive cost** or **Normal cost** based on a threshold.
- Ranks buildings from highest to lowest total cost.

## Requirements
- Python 3.x
- No external libraries are required.

## Data and Settings
- `buildings`: names of the campus buildings.
- `electricity`: electricity readings for each building, organized by day.
- `water`: water readings for each building, organized by day.
- `electricity_rate`: cost per electricity unit (`8` in this example).
- `water_rate`: cost per water unit (`2` in this example).
- `limit`: total-cost threshold (`2500` in this example).

The sample assumes each inner list contains three readings and that the electricity and water lists correspond to the same buildings and days.

## How It Works
1. The program loops through each building.
2. It adds the electricity and water readings for that building.
3. It multiplies each consumption total by its respective rate to calculate costs.
4. It combines electricity and water costs into a total cost and saves that value.
5. It calculates the percentage change in electricity usage between the first and third readings.
6. It compares total cost with the limit and prints a status.
7. It sorts the buildings and their costs in descending order, then prints the ranking.

## Source Code
Save the program in a file named `campus_energy_water_audit.py`.

```python
buildings = ["Block A", "Block B", "Block C"]

electricity = [
    [100, 120, 110],
    [150, 160, 170],
    [80, 90, 100]
]

water = [
    [500, 550, 520],
    [700, 750, 800],
    [400, 420, 450]
]

electricity_rate = 8
water_rate = 2
limit = 2500
costs = []

for i in range(len(buildings)):
    energy_total = 0
    water_total = 0

    for j in range(len(electricity[i])):
        energy_total = energy_total + electricity[i][j]
        water_total = water_total + water[i][j]

    energy_cost = energy_total * electricity_rate
    water_cost = water_total * water_rate
    total_cost = energy_cost + water_cost
    costs.append(total_cost)

    change = ((electricity[i][2] - electricity[i][0])
              / electricity[i][0]) * 100

    print("Building:", buildings[i])
    print("Electricity used:", energy_total)
    print("Water used:", water_total)
    print("Electricity cost:", energy_cost)
    print("Water cost:", water_cost)
    print("Total cost:", total_cost)
    print("Electricity change:", round(change, 2), "%")

    if total_cost > limit:
        print("Status: Excessive cost")
    else:
        print("Status: Normal cost")

    print()

for i in range(len(costs)):
    for j in range(i + 1, len(costs)):
        if costs[j] > costs[i]:
            costs[i], costs[j] = costs[j], costs[i]
            buildings[i], buildings[j] = buildings[j], buildings[i]

print("Buildings ranked by total cost:")

for i in range(len(buildings)):
    print(i + 1, buildings[i], "-", costs[i])
```

## How to Run
1. Install Python 3 if needed.
2. Save the code as `campus_energy_water_audit.py`.
3. Open a terminal or command prompt in the folder containing the file.
4. Run:

```bash
python campus_energy_water_audit.py
```

On some systems, use `python3 campus_energy_water_audit.py`.

## Sample Output

```text
Building: Block A
Electricity used: 330
Water used: 1570
Electricity cost: 2640
Water cost: 3140
Total cost: 5780
Electricity change: 10.0 %
Status: Excessive cost

Building: Block B
Electricity used: 480
Water used: 2250
Electricity cost: 3840
Water cost: 4500
Total cost: 8340
Electricity change: 13.33 %
Status: Excessive cost

Building: Block C
Electricity used: 270
Water used: 1270
Electricity cost: 2160
Water cost: 2540
Total cost: 4700
Electricity change: 25.0 %
Status: Excessive cost

Buildings ranked by total cost:
1 Block B - 8340
2 Block A - 5780
3 Block C - 4700
```

## Customization
- Add buildings to `buildings` and add matching rows to both `electricity` and `water`.
- Update the rates to match your local utility tariffs.
- Change `limit` to set a different excessive-cost threshold.
- Update the readings to include the days you want to audit.

## Important Notes
- The program flags a building when its total cost is **strictly greater than** `limit`; a total equal to the limit is classified as normal.
- The electricity percentage change compares the first and third readings, not the average or total. The calculation assumes the first electricity reading is not zero and that at least three readings are available.
- The `water` loop uses the same index range as `electricity`, so corresponding rows should have the same number of readings.
- The ranking is based on **total cost**, from highest to lowest. It is not a separate energy-efficiency or water-efficiency score.
- Consumption units and currency are not specified in the code. Confirm the units and rates before using this for real audits.

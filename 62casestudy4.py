# Water Distribution Fairness Analysis: Analyse area-wise water supply across several days, calculate shortages against demand,
#  compare distribution levels, and identify the most underserved areas. 
areas = ["Area A", "Area B", "Area C"]
demand = [100, 120, 80]

supply = [
    [90, 80, 100],
    [70, 90, 60],
    [80, 75, 80]
]

for i in range(len(areas)):
    total = 0

    for j in range(len(supply[i])):
        total = total + supply[i][j]

    total_demand = demand[i] * len(supply[i])
    shortage = total_demand - total
    average = total / len(supply[i])

    print("Area:", areas[i])
    print("Total demand:", total_demand)
    print("Total supply:", total)
    print("Average supply:", round(average, 2))
    print("Shortage:", shortage)

    if shortage > 0:
        print("Status: Underserved")
    else:
        print("Status: Sufficient supply")

    print()
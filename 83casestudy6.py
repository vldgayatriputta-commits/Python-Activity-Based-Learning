# Food Supply Chain Stock Reconciliation: Compare quantities received, distributed, damaged, and remaining across several locations;
#  identify discrepancies and calculate replenishment requirements. 
locations = ["Location A", "Location B", "Location C"]
received = [500, 400, 300]
distributed = [350, 250, 200]
damaged = [20, 30, 10]
remaining = [120, 100, 90]

for i in range(len(locations)):
    calculated = received[i] - distributed[i] - damaged[i]

    print("Location:", locations[i])
    print("Received:", received[i])
    print("Distributed:", distributed[i])
    print("Damaged:", damaged[i])
    print("Recorded stock:", remaining[i])
    print("Calculated stock:", calculated)

    if calculated == remaining[i]:
        print("Status: Stock matches")
    else:
        print("Status: Discrepancy detected")
        print("Difference:", calculated - remaining[i])

    if remaining[i] < 100:
        print("Replenishment required:", 100 - remaining[i])
    else:
        print("Replenishment not required")

    print()
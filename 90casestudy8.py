# Integrated Campus Energy and Water Audit: Analyse consumption across buildings and days, calculate costs and percentage changes,
#  identify excessive consumption, and rank buildings using a specified scoring method. 
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
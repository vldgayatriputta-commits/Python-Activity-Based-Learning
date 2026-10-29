# Environmental Monitoring Data Analyzer: Analyse nested lists of air-quality or water-quality readings, calculate averages
#  and extremes, and classify observations using supplied threshold values.
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
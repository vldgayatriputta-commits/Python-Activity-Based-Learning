# Disaster Relief Supply Allocation: Compare stock lists against area-wise requirements, prioritize urgent shortages,
#  allocate limited supplies according to a prescribed policy, and calculate remaining unmet demand. 
areas = ["Area A", "Area B", "Area C", "Area D"]
required = [100, 80, 60, 50]
priority = [3, 1, 2, 1]
stock = 200

for i in range(len(areas)):
    for j in range(i + 1, len(areas)):
        if priority[j] > priority[i]:
            priority[i], priority[j] = priority[j], priority[i]
            required[i], required[j] = required[j], required[i]
            areas[i], areas[j] = areas[j], areas[i]

for i in range(len(areas)):
    if stock >= required[i]:
        allocated = required[i]
    else:
        allocated = stock

    stock = stock - allocated
    shortage = required[i] - allocated

    print("Area:", areas[i])
    print("Required:", required[i])
    print("Allocated:", allocated)
    print("Unmet demand:", shortage)
    print()

print("Remaining stock:", stock)
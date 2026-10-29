# Multi-Route Courier Dispatch Planning: Process package weights, destination zones, vehicle capacities, and delivery priorities;
#  allocate packages to vehicles and identify packages that cannot be dispatched
packages = [
    ("P101", 8, "Urgent"),
    ("P103", 6, "Urgent"),
    ("P105", 10, "Urgent"),
    ("P102", 12, "Normal"),
    ("P104", 15, "Normal")
]

capacity = [20, 25]
load = [0, 0]

for package in packages:
    package_id, weight, priority = package
    assigned = False

    for i in range(len(capacity)):
        if load[i] + weight <= capacity[i]:
            load[i] = load[i] + weight
            print("Package:", package_id)
            print("Priority:", priority)
            print("Assigned to Vehicle", i + 1)
            assigned = True
            break

    if assigned == False:
        print("Package:", package_id)
        print("Status: Cannot be dispatched")

    print()

for i in range(len(capacity)):
    print("Vehicle", i + 1, "load:", load[i])
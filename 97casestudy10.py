#Smart Campus Incident and Maintenance Prioritization: Classify hypothetical maintenance reports using severity,
#  location, and reported frequency; rank cases using predefined rules and generate a priority summary. 
incidents = [
    ("Water Leakage", "Hostel", 3, 4),
    ("Broken Fan", "Classroom", 1, 2),
    ("Electrical Fault", "Laboratory", 3, 3),
    ("Damaged Bench", "Classroom", 1, 1)
]

for incident in incidents:
    name, location, severity, frequency = incident
    score = severity * 10 + frequency * 5

    print("Incident:", name)
    print("Location:", location)
    print("Priority score:", score)

    if severity == 3:
        print("Priority: High")
    elif severity == 2:
        print("Priority: Medium")
    else:
        print("Priority: Low")

    print()
# Smart Campus Incident and Maintenance Prioritization

## Overview
The **Smart Campus Incident and Maintenance Prioritization** system is a Python program that analyzes hypothetical campus maintenance incidents based on severity, location, and reported frequency. It calculates a priority score and classifies each incident as High, Medium, or Low priority.

## Features
- Stores incident details using Python tuples.
- Records incident names, locations, severity, and frequency.
- Calculates a priority score for each incident.
- Classifies incidents into High, Medium, and Low priority levels.
- Displays a priority summary for each reported incident.

## Requirements
- Python 3.x
- No external libraries required.

## Input Details
Each incident contains four values:

- **Incident name:** The reported maintenance problem.
- **Location:** The campus area where the incident occurred.
- **Severity:** A value indicating the seriousness of the incident.
- **Frequency:** The number or level of times the incident has been reported.

## Priority Scoring Method
The program calculates the priority score using the following formula:

`Priority Score = (Severity × 10) + (Frequency × 5)`

Severity determines the priority category, while frequency contributes to the numerical score.

### Priority Classification

| Severity | Priority |
|---|---|
| 3 | High |
| 2 | Medium |
| 1 | Low |

## How It Works
1. The program stores incidents in a list of tuples.
2. A loop processes each incident individually.
3. Tuple unpacking extracts the incident name, location, severity, and frequency.
4. The priority score is calculated using the predefined formula.
5. Conditional statements classify the incident based on severity.
6. The incident details, score, and priority category are printed.

## Source Code
Save the Python program as `smart_campus_prioritization.py`.

```python
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
```

## How to Run
1. Install Python 3 if it is not already installed.
2. Save the code as `smart_campus_prioritization.py`.
3. Open a terminal or command prompt in the project folder.
4. Execute:

```bash
python smart_campus_prioritization.py
```

If required, use `python3` instead of `python`.

## Sample Output

```text
Incident: Water Leakage
Location: Hostel
Priority score: 50
Priority: High

Incident: Broken Fan
Location: Classroom
Priority score: 20
Priority: Low

Incident: Electrical Fault
Location: Laboratory
Priority score: 45
Priority: High

Incident: Damaged Bench
Location: Classroom
Priority score: 15
Priority: Low
```

## Customization
- Add new incidents to the `incidents` list.
- Update the severity and frequency values as needed.
- Modify the scoring formula to reflect campus maintenance policies.
- Change the severity conditions to adjust priority classifications.

## Limitations
- The program processes hypothetical data entered directly into the source code.
- Incidents are displayed in input order rather than sorted by priority score.
- Location is displayed but does not affect the priority score.
- The priority category depends only on severity, not on the combined score.
- No database, graphical interface, or automated notification system is included.

## Future Enhancements
- Sort incidents by priority score.
- Include location-based risk factors in the scoring method.
- Store incident reports in a database.
- Add a graphical dashboard for maintenance staff.
- Generate notifications for high-priority incidents.
- Allow users to submit reports through a mobile or web application.

## Conclusion
This project demonstrates how Python tuples, loops, arithmetic operations, and conditional statements can be used to classify campus maintenance incidents. It provides a foundation for developing a more advanced campus maintenance management system.

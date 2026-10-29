#Student Timetable Conflict Detection: Compare course schedules represented by strings and tuples, detect overlapping periods, 
# identify unavailable rooms, and validate a proposed timetable. 
timetable = [
    ("Python", "Monday", 1, "R101"),
    ("Maths", "Monday", 2, "R102"),
    ("Web", "Monday", 1, "R103"),
    ("English", "Tuesday", 1, "R101"),
    ("AI", "Monday", 1, "R101")
]

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        subject1, day1, period1, room1 = timetable[i]
        subject2, day2, period2, room2 = timetable[j]

        if day1 == day2 and period1 == period2:
            if room1 == room2:
                print("Room conflict detected")
                print("Subjects:", subject1, "and", subject2)
                print("Day:", day1)
                print("Period:", period1)
                print("Room:", room1)
            else:
                print("No room conflict between",
                      subject1, "and", subject2)

print("Timetable checking completed")
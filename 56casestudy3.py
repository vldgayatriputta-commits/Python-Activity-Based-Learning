#Student Group Formation with Score Balancing: Arrange students using a list of scores and allocate them into groups of specified sizes while
#  minimizing differences between group totals under defined allocation rules. 
students = ["Asha", "Balu", "Charan", "Divya", "Esha", "Farhan"]
scores = [90, 75, 85, 60, 80, 70]

group1 = []
group2 = []
total1 = 0
total2 = 0

for i in range(len(scores)):
    if total1 <= total2:
        group1.append(students[i])
        total1 = total1 + scores[i]
    else:
        group2.append(students[i])
        total2 = total2 + scores[i]

print("Group 1:", group1)
print("Group 1 total:", total1)
print("Group 2:", group2)
print("Group 2 total:", total2)

difference = total1 - total2

if difference < 0:
    difference = -difference

print("Difference between groups:", difference)

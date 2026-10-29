# Examination Result and Grace-Mark Validation: Process marks across multiple subjects,
#  apply subject-wise pass criteria and a specified grace-mark policy, and generate final classifications without exceeding maximum marks. 
students = ["Asha", "Balu", "Charan", "Divya"]
marks = [85, 45, 92, 68]

total = 0
highest = marks[0]
lowest = marks[0]

for i in range(len(students)):
    total = total + marks[i]

    if marks[i] > highest:
        highest = marks[i]

    if marks[i] < lowest:
        lowest = marks[i]

    print("Student:", students[i])
    print("Marks:", marks[i])

    if marks[i] >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print()

average = total / len(marks)

print("Total marks:", total)
print("Average marks:", round(average, 2))
print("Highest marks:", highest)
print("Lowest marks:", lowest)
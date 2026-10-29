# Attendance Recovery Computation: Calculate current attendance percentages and determine the minimum consecutive 
# classes required to reach an eligibility threshold under different future attendance scenarios. 
books = ["Python", "Java", "HTML", "CSS", "Database"]
available = [5, 0, 3, 2, 0]

search_book = input("Enter book name: ")
found = False

for i in range(len(books)):
    if books[i].lower() == search_book.lower():
        found = True
        print("Book:", books[i])
        print("Available copies:", available[i])

        if available[i] > 0:
            print("Status: Book is available")
        else:
            print("Status: Book is not available")

if found == False:
    print("Book not found in the library")

print("Library checking completed")
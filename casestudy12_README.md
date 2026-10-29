# Library Book Availability Checker

## Overview
The **Library Book Availability Checker** is a simple Python program that allows users to search for a book by name and check how many copies are available in the library. It displays the book's availability status or informs the user if the requested book is not listed.

## Features
- Stores book names and available copy counts using Python lists.
- Accepts a book name from the user.
- Performs a case-insensitive search.
- Displays the number of available copies.
- Indicates whether a book is available or unavailable.
- Displays a message when a book is not found.

## Requirements
- Python 3.x
- No external libraries required.

## Data Details
The program maintains two lists:

- `books`: Contains the names of the books.
- `available`: Contains the number of available copies corresponding to each book.

| Book | Available Copies |
|---|---:|
| Python | 5 |
| Java | 0 |
| HTML | 3 |
| CSS | 2 |
| Database | 0 |

## How It Works
1. The program initializes the book names and their available copy counts.
2. It asks the user to enter a book name.
3. The entered name is compared with each book name after converting both to lowercase.
4. If a matching book is found, its name and available copies are displayed.
5. If the available count is greater than zero, the program reports that the book is available. Otherwise, it reports that the book is unavailable.
6. If no matching book is found, the program displays a book-not-found message.
7. Finally, it prints a completion message.

## Source Code
Save the program as `library_book_checker.py`.

```python
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
```

## How to Run
1. Install Python 3 on your computer.
2. Save the code as `library_book_checker.py`.
3. Open a terminal or command prompt in the folder containing the file.
4. Run:

```bash
python library_book_checker.py
```

If necessary, use `python3 library_book_checker.py`.

## Sample Output

### Example 1: Book available

```text
Enter book name: Python
Book: Python
Available copies: 5
Status: Book is available
Library checking completed
```

### Example 2: Book unavailable

```text
Enter book name: Java
Book: Java
Available copies: 0
Status: Book is not available
Library checking completed
```

### Example 3: Book not found

```text
Enter book name: C++
Book not found in the library
Library checking completed
```

## Customization
- Add new books to the `books` list.
- Add the corresponding copy counts to the `available` list.
- Update the available quantities when books are borrowed or returned.
- Ensure both lists contain the same number of elements.

## Limitations
- The program uses fixed data stored in the source code.
- It does not record borrowing or returning transactions.
- It does not maintain borrower details or due dates.
- It does not use a database to store library records.

## Future Enhancements
- Add book borrowing and returning features.
- Store book details in a database.
- Display all available books.
- Include author names and book IDs.
- Add a graphical user interface.
- Track borrowed books and return dates.

## Conclusion
The Library Book Availability Checker demonstrates Python lists, loops, conditional statements, user input, and case-insensitive string comparison. It provides a simple foundation for developing a library management system.

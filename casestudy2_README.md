# Text Compression Using Character Runs

## Project Description
This Python program compresses text by counting consecutive repeated characters. It stores each character followed by the number of times it appears consecutively. This method is called run-length encoding.

## Objectives
- To compress text containing consecutive repeated characters.
- To count repeated characters.
- To compare the original text length with the compressed text length.
- To determine whether compression reduces the text size.

## Technologies Used
- **Programming Language:** Python
- **Concepts:** Strings, Loops, Conditional Statements, String Concatenation, `len()` Function

## How the Program Works
1. The program stores the input text in the variable `text`.
2. It initializes an empty string named `compressed` and sets `count` to `1`.
3. A loop checks whether each character matches the previous character.
4. If the characters match, the count increases.
5. If they differ, the previous character and its count are added to the compressed string, and the count resets to `1`.
6. After the loop, the final character and its count are added.
7. The program prints the original text, compressed text, and both lengths.
8. Finally, it checks whether the compressed text is shorter than the original text.

## Sample Input
```python
text = "aaabbccccdd"
```

## Sample Output
```text
Original text: aaabbccccdd
Compressed text: a3b2c4d2
Original length: 11
Compressed length: 8
Compression is beneficial
```

## Advantages
- Simple and beginner-friendly.
- Reduces the length of strings with repeated consecutive characters.
- Demonstrates a basic text compression technique.

## Limitations
- It works best when characters repeat consecutively.
- The compressed form may be longer for text with few or no repeated characters.
- This is a simple educational example, not a complete general-purpose compression system.

## How to Run
1. Install Python on your computer.
2. Save the program in a file named `text_compression.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

```bash
python text_compression.py
```

## Conclusion
This project demonstrates run-length encoding by replacing consecutive repeated characters with the character and its count. It also compares the original and compressed lengths to check whether the compression is beneficial.

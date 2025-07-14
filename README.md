assignment 4
Task 1: Read a File and Handle Errors
try: Starts error-checking block.
open('sample.txt', 'r'): Tries to open the file in read mode.
read(): Reads the entire content of the file.
print(): Displays the content.
close(): Closes the file after reading.
except IOError: If file is missing or can’t be opened, shows: File not found

Task 2: Write and Append Data to a File
input() – Takes user input and stores it.
open("output.txt", "w") – Creates or overwrites the file and writes the first input.
open("output.txt", "a") – Appends the second input to the same file.
open("output.txt", "r") – Reads the final content of the file.
print(content) – Displays the full file content on screen.

ASSIGNMENT 5
Task 1: Create a Dictionary of Student Marks
Creates a dictionary called student
– It stores student names as keys and their marks as values.
   Example: 'pratham': 90
Takes input from the user (asks for a student name).
Checks if the entered name exists in the dictionary:
  If yes, it prints the name and their marks.
  If not, it prints "student not found".

Task 2: Demonstrate List Slicing
Creates a list l with numbers from 1 to 10.
Extracts the first 5 elements using slicing:
 n = l[0:5]  # gives [1, 2, 3, 4, 5]
Prints the original list and the extracted part.
Reverses the extracted part using .reverse() and prints it.

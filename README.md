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

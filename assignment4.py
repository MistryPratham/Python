# Task 1: Read a File and Handle Errors

try:
    module5task = open('sample.txt','r')
    reading_file = module5task.read()
    print(reading_file)
    module5task.close()
except IOError:
    print("File not found")

# Task 2: Write and Append Data to a File

try:
    m = input("Enter the text to write to the file: ")
    module5task = open('output.txt','w')
    writing_file = module5task.write(m)
    print("data is successfully written to file")
    module5task.close()
except IOError:
    print("File not found")
try:
    m = input("Enter additional text to append: ")
    module5task = open('output.txt','a')
    writing_file = module5task.write(m)
    print("data is successfully append to file")
    module5task.close()
except IOError:
    print("File not found")
try:
    module5task = open('output.txt','r')
    reading_file = module5task.read()
    print(reading_file)
    module5task.close()
except IOError:
    print("File not found")
# Task 1: Check if a Number is Even or Odd

number = int(input("Enter a number: "))
if number % 2 == 0 :
    print("number is even")
else:
    print("number is odd")

# Task 2: Sum of Integers from 1 to 50 Using a Loop

n=0
for i in range(1,51):
    n += i
    print("The sum of numbers from 1 to 50 is:", n)

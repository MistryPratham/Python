# Task 1: Calculate Factorial Using a Function

def factorial():
    n=int(input("Enter the number: "))
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print("factorial number is:",factorial())


# Task 2: Using the Math Module for Calculations

import math
n=int(input("Enter the number: "))
print(math.sqrt(n))
print(math.log(n))
print(math.sin(n))

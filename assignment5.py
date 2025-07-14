# Task 1: Create a Dictionary of Student Marks

student = {'pratham':90,'preet':30,'priyanshi':99,'pavani':50,'parth':70}
n = input('enter a student name: ')
if n in student:
 print(n, "marks:", student[n])
else:
 print('student not found')


# Task 2: Demonstrate List Slicing

l = [1,2,3,4,5,6,7,8,9,10]
n = l[0:5]
print("Original List: ",l)
print("Extracted first element: ",n)
n.reverse()
print("Reversed extracted element: ",n)

#.    Write a program to intalize a number and find odd or even
# Python program to check if the input number is odd or even
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


#10.    Write a program to find average of 5 subjects.


english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100

print("\nTotal Marks = %.2f"  %total)
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)

   
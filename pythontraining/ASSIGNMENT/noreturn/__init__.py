
def add_one(x):
     # No return statement at all
     result = x + 1
     return result

value = add_one(5)
print(value)

#7.    Write a program for addition, subtraction, multiplication, division and modulus. By using nested if


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)

# 8.    Write a program to find greatest of 2 numbers.
num1=int(input("enter first number"))
num2=int(input("enter second number"))
print(max(num1,num2),"is greater")
print(min(num1,num2),"is lesser")


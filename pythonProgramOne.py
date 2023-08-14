# Project Name: Program One-Data Types and if Statements
#
# Name: Vanessa Barajas
#
# Date: 8-13-2023
#
# Objective: Write a "largest of three" program in Python using one nested if statement, a compound if statement,
# and another solution from ChatGPT use int, string, double, and bool variable types demonstrate primitive variable
# usage by getting and displaying username, outputting the quotient of the first input number by the second input
# number display, print(), the types of all variables used in the program.
#
#
print("\n Welcome to the Largest of Three Program!\n")
#
# Below is where I will include variable declarations
# Integer variable declarations
num1 = 0
num2 = 0
num3 = 0
largest_num = 0
#
# String variable declaration
user_name = ""

# Double variable declaration
result_of_division = 0.0

# Boolean variable declaration
play_again = False

# Outputs
print("\n num1 is of type:" + str(type(num1)))
print("\n num2 is of type:" + str(type(num2)))
print("\n num3 is of type:" + str(type(num3)))
print("\n user_name is of type:" + str(type(user_name)))
print("\n result_of_division is of type:" + str(type(result_of_division)))
print("\n play_again is of type:" + str(type(play_again)))

# User inputs for integers
num1 = input("\n Please enter the first whole (integer) number: ")
print("\n num1= " + num1)
num2 = input("\n Please enter the second whole (integer) number: ")
print("\n num2= " + num2)
num3 = input("\n Please enter the third whole (integer) number: ")
print("\n num3= " + num3)

# Obtain username
user_name = input("Please enter your name: ")
print("Hi" + user_name + ", Welcome to the largest of three game! ")

num1 = 39
num2 = 24
num3 = 77

# Nested if statement
if num1 > num2:
    if num1 > num3:
        largest_num = num3
    else:
        largest_num = num1
else:
    if num2 > num3:
        largest_num = num2
    else:
        largest_num = num3

print("\n\n The largest of three is: " + str(largest_num))

# Compound if statement
n1 = 7
n2 = 3
n3 = 6
n4 = 8
if n1 < n2 and n1 <n3:
    print("n\n" + str(n1) + "is the smallest.")
else:
    print("\n\n" + str(n1) + "is not the smallest.")





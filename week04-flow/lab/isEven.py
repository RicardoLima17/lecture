

#1. Write a program (isEven.py) that asks the user to enter in a number, and the 
# program will tell the user if the number is even or odd.
# Author Ricardo


# type any number
number = int(input("enter a number "))

# number divided by 2
if (number % 2) == 0:
    print ("{} in an even number".format(number))

# if is not number divided by 2 print this statement
else:
    print ("{} in an odd number".format(number))
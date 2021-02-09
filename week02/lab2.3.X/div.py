
# Author Ricardo

# type the number1
number1 = int(input('enter first number: '))

# type the number1
number2 = int(input('enter the number you want to divide by: '))

# calculation and all the number will be int
result = int(number1 / number2)

# reminder
remainder = number1%number2

# print 
print ("{} diveded by {} is {} with remainder {} " .format(number1, number2, result, remainder))
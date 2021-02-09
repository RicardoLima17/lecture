# read in a name and print it out
# Author: Ricardo Rodrigues

# we must convert to number be real number to add a real number
number =  int(input('please enter your number:'))
newNumber = number + 1
print ('{} plus one is {}' .format(number, newNumber))

name = input("Enter your name:")
print('Hello '+ name + '\nNice to meet you')
# or you could do this with format
print('Hello {}\nNice to meet you'.format(name))
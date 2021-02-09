
#Author Ricardo

# This program prints out a random fruit
import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')


# we want a random number between 0 = apple and lenght-1 = Pear
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))

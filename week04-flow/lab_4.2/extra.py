


import random
# I programming the general case
number = random.randint(1, 100)

while True:

    print('Guess a number between 1 and 100')
    
    guess = input()
    i = int(guess)

    if i == number:
        print('You won!!!')

        break

    elif i < number:
               print('Try Higher')
    elif i > number:
               print('Try Lower')

print('if you gussed less than 6 times you won')
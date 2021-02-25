
# Author Ricardo

numberToGuess = 20
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
 print ("Wrong")
guess = int(input("Please guess again:"))
print ("Well done! Yes the number was ", numberToGuess)
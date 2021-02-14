# Extra (I will not give the answer to these)
# 3. In practice the percentages are rounded ie 69.5 gets rounded to 70 so is equal to a Distinction.
# How would you modify the program in 1 to deal with this? I see two ways.

# Author Ricardo

import math


number = float(input("Enter the percentages "))



percentage = number

#print('{} your mark is {}'.format(abs(number), math.floor(percentage)))


   
if (percentage >= 0 and percentage< 40):
    print('{} mark is {}'.format(abs(number), math.ceil(percentage)))
    print ("Fail")

elif (percentage > 40 and percentage < 50):
    print("Pass")

elif (percentage >= 50 and percentage < 60):
    print("Merit 1")
 bnjkh u80o[:~P<]
elif (percentage >= 60 and percentage < 70):
    print("Merit2")

elif (percentage >= 70 and percentage < 100.01):
    print("Distinction")

else:
     print("Please enter a number between 0 and 100")




   




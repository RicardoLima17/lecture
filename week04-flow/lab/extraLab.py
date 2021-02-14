# Extra (I will not give the answer to these)
# 3. In practice the percentages are rounded ie 69.5 gets rounded to 70 so is equal to a Distinction.
# How would you modify the program in 1 to deal with this? I see two ways.

# Author Ricardo

import math


percentage = float(input("Enter the percentages "))



 

print('{} your mark is {}'.format(abs(percentage), math.ceil(percentage)))


   
if 0 >=   percentage < 39:
     print ("Fail")

elif 40 >= percentage < 49:
    print("Pass")

elif 50 >=  percentage < 59:
    print("Merit 1")

elif 60 >=  percentage < 70:
    print("Merit2")

elif 70 >= percentage <= 100:
    print("Distinction")

else:
     print("Please enter a number between 0 and 100")

endprogram = 


   






percentage = float(input("Please enter the student's percentage mark: "))


import math

# convert to positive and round to 39.5 to 40
#print('{} your mark is {}'.format(abs(percentage), math.ceil(percentage)))

# Error handling that the number entered is valid
if (percentage < 0) or (percentage > 100):
    print('Please enter a number between 0 and 100')

#less than 40
if percentage < 39.49 :  
    print('Fail')

#between 40 and 49
elif percentage < 49.49:  
    print('Pass')

#between 50 and 59
elif percentage < 59.49:  
    print('Merit 1')

#between 60 and 69
elif percentage < 69.49:  
    print('Merit 2')

#only other option is between 70 and 100 
elif percentage < 100:  
    print('Distinction')

 #100.1 to infinity 
else:
    print('wrong mark') 

print('{} your mark is {}'.format(abs(percentage), math.ceil(percentage)))
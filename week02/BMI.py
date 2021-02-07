# BMI 
# Author: Ricardo Rodrigues

# declare variable, i am using a floot to type a decimal, 'read the message and type'
weight =  float(input('please enter your weight in kg: '))
height =   float(input('please enter your Height in centimeter: '))

# BMI is the variable of what did you type for weight and height 
BMI =(weight / (height ** 2)) * 10000

# Conditions if: the result is less than 18.5 
if BMI < 18.5:
        print("A person with a BMI of " + str((round(BMI,2))) + " is underwieght ")

# Conditions if: the result is iqual or less than 24.99
elif BMI <= 24.99:
        print("A person with a BMI of " + str((round(BMI,2))) + " is normal weight ")

# Conditions if: the result is high than 24.9999 print this statment
else:
        print("A person with a BMI of " + str((round(BMI,2))) + " is overweight ")

input('Please press Enter to exit')




# print message and follow the information to next action 
print (' please enter your weight in kg: ')

# declare variable, i am using a floot to type a decimal, 'read the message and type'
weight =  float(input(' '))

# print message and follow the information to next action 
print (' please enter your height in kg: ')

# declare variable, i am using a floot to type a decimal, 'read the message and type'
height =   float(input(' '))

# Convert cm to meter
height = height/100

# BMI show the calculation
BMI = weight / (height**2)

# print BMI and I used a function round 2 decimal 
print ('Your BMI: ', (round(BMI,2)))

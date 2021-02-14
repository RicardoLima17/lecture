
# 2. Write a program (grade.py) that reads in a students percentage mark and
# prints out corresponding the grade (the program should check that the percentage is valid:

# Author Ricardo

percentage = float(input("Enter the percentages "))

   
if (percentage > 0 and percentage < 40):
    print ("Fail")

elif (percentage > 40 and percentage < 50):
    print("Pass")

elif (percentage > 50 and percentage < 60):
    print("Merit 1")

elif (percentage > 60 and percentage < 70):
    print("Merit2")

elif (percentage > 70 and percentage < 100.01):
    print("Distinction")

else:
    print("Please enter a number between 0 and 100")

        
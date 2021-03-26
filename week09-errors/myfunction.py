# a module of useful functions

"""
function that returns the factorial number of int ie
7! = 7x6x5x4x3x2x1 = 5040
"""

def factorial(num):
    if num== 1:
        return 1
    factorial = 1
    num +=1
    for i in range(1,num):
        factorial *= i
    return factorial 

if __name__== "__main__":
     print("in my function ", __name__)
     assert factorial(7)==5040
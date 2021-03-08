
# more messing with function
# flexible arguments

print("hi", 55, 343,[],{}, sep=":")

# flexible number of arguments

def average(*numbers):
    sumof = sum(numbers)
    return sumof / len(numbers)

ave = average(12, 12, 12, 34234, 121,34)    
print("average is ", ave)


# flexible number or named arguments
def fun(arg1 = 0, arg2 = 1 ):
    return arg1 - arg2

print(fun(10, 2))


def funkyArgs(**args):
    print (args)
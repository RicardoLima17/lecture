
# more messing with functions
# variable scope

var = 10

def cube(num):
    var = 66
    print("in the function var is ", var)
    return num **3

cube(22)
print("outside the function var is ", var)

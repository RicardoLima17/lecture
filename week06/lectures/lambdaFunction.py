# more messing with functions
# Anonymous functions

#def doubler (num):
    #return num * 2


#def tripler (num):
    #return num * 3



# print True only doubler just IF/ False print tripler
isMax = True
if isMax:
    # when use lambda the function does not have name. you can use the lambda and delet the function
    fun = lambda num : num * 2
else:
    fun = lambda num : num * 3

var = fun(10)
print (var)

# sorted
list = [22, 33, 11, 1, 44]
print (list)
newList = sorted(list, reverse=False)
print (newList)


# sort dictionary
data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper', 'YOB': 1006},
        {'first': 'Alan', 'last': 'Turing', 'YOB': 1912}]

#def sortFun(item):
   # print ("in sortFun")
   # return item['YOB']

#print (data)    when use lambda i do not need my function def sortFun(item)
newData = sorted(data, key = lambda item : item['last'])
for item in newData:
   print (item)

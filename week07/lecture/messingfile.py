# program is demosntrate f:
# as part of my lecture

# create a new file "W"
with open(".\lecture1.txt", "w") as f:
    print ("create a file") 

with open("datatest.txt", "rt") as f :
    data = f.read()
    print (data)

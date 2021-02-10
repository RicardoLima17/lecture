

#Author Ricardo

# type a negative and decimal number
number = float(input(" Please eneter any amount "))

# convert to positve
absolute = abs(number)

# convert to cents and use int to remove .0 
result = int(absolute * 100)

print ("That amount in cent is {}:" .format(result))
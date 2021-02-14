
# Author Ricardo


# strip() normalised the space and lowe() or upper(), change the letter to lower case
rawString = input("please enter a string: ")

# converts all the letters to lower case and remove the space characters
normalisedString = rawString.strip() .lower()
print("That String normalised is: {}".format(normalisedString))

# count the characters before and after 
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)
print("we reduced the input string from {} to {} characters".format(lenghtOfRawString, lenghtOfNormalised ))
# this program is to show how you can use try except


# filename = 'data.txt'

import sys

filename = sys.argv[1]

try:
    with open(filename) as f:
        print (f.read())
except:
        print('a exception occured')
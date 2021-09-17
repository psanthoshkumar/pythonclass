# python3 sum.py
# enter a value: 20
# enter b value: 30
# Sum of 20, 30 is : 50

# python3 sum.py 20 30
#           0     1  2
# Sum of 20, 30 is : 50

import sys


def sum(a, b):
    return a+b


a = eval(sys.argv[1])
b = eval(sys.argv[2])
# c = eval(sys.argv[0])

# print('0th place value: {}'.format(c))
print('a value is: {} and b value is : {}'.format(a, b))
print('sum value: {}'.format(sum(a, b)))

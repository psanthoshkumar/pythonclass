import random

# number = eval(input('Enter a number: '))

number = random.randint(100, 200)
print("Random number is: {}".format(number))

if number % 2 == 0:
    print("{} is Even number".format(number))
else:
    print('{} is odd number'.format(number))
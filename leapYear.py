year = eval(input("Enter a year: "))

if year % 4 == 0:
    print('{} is leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))

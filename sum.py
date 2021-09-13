def sum(a, b):
	return a+b

a = eval(input('enter a value: '))
b = eval(input('enter b value: '))

print('a type is: {}'.format(type(a)))
print('b type is: {}'.format(type(b)))

print(f'sum of {a}, {b} is: {sum(a, b)}')

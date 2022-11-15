'''
Write a function that takes three arguments: a float, a float, and a string.

The function should recognize at least the following four options for the string: +, -, *, /.

The function will return the first float argument operated on by the second float argument, with the math operation determined by the string argument.
'''

'''
calculate(10,7,'+')

The function should return 17.
'''

def calculate(x, y, operator):
	if operator == "+":
		return x + y
	elif operator == "-":
		return x - y
	elif operator == "*":
		return x * y
	elif operator == "/":
		return x / y
	return x

print(calculate(10, 7, "+"))

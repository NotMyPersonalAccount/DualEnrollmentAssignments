import math

def factorial_std(number):
	return math.factorial(number)

def factorial(number):
	total = 1
	for i in range(1, number + 1):
		total *= i
	return total

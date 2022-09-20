'''
The Factorial of an integer is defined as follows:  take the integer, and multiply it by itself minus one, then itself minus two, and so on, until you hit one.

So, for example, the factorial of 7 (written as x!) is equal to 7 * 6 * 5 * 4 * 3 * 2 * 1, or 5040.

 

For this exercise, define two different custom functions, each of which take one argument, an integer.

Each one should return the factorial of the integer argument.

However, one of your custom functions should rely on the Python standard library to calculate the factorial, and the other should use your custom code to calculate it, without using the Python standard library!
'''

import math

def factorial_std(number):
	return math.factorial(number)

def factorial(number):
	total = 1
	for i in range(1, number + 1):
		total *= i
	return total

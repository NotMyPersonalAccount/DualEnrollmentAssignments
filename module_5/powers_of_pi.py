'''
We're going to write a function that takes one integer argument, which I'll call n.

This function should return a list of length n, where the first element is a decimal approximation of pi, the second element is pi^2, the third element is pi^3, and so on.
'''

from math import pi

def powers_of_pi(n):
	list = []
	for i in range(1, n+1):
		list.append(pi**i)
	return list

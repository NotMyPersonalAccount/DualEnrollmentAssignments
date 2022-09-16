'''
The Fibonacci Sequence is an integer (whole number) sequence calculated in the following manner:

The first two numbers in the sequence are 0, 1.

Every number in the sequence after that is calculated by adding the two previous numbers in the sequence.

Hence, the first 13 values in the Fibonacci Sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.

Write a function that takes a single integer argument, and returns the number at that position in the Fibonacci sequence.  (For consistency with how the sequence is usually defined, let's call the very first number in the sequence, which is 0, the zeroeth number in the sequence.  So the first number in the sequence will be 1).
'''

'''
fib(8)

Would return 21.
'''

def fib(x):
	a = 0
	b = 1
	for i in range(x):
		a = a + b
		b = a - b
	return a
print(fib(8))

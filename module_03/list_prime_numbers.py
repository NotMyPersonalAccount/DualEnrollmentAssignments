'''
The prime numbers are those whole numbers which are evenly divisible by exactly two whole numbers: themselves, and 1.

So, the first 10 prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

We're going to write a program that creates a list holding the first N prime numbers, where N is given by the user.

So, first you will ask the user for a number, which will be N.  Then, do whatever it takes using loops and append to create a list that holds the first N prime numbers!

Finally, print this list.
'''

'''
Enter the number of primes to compute: 10

The first 10 prime numbers are:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 27]
'''

x = int(input("Enter the nu,ber of primes to compute: "))
numbers = []

def is_prime(n):
	for j in range(2, n // 2 + 1):
		if n % j == 0:
			return False
	return True

i = 2
while len(numbers) != x:
	if is_prime(i):
		numbers.append(i)
	i += 1
print(numbers)	

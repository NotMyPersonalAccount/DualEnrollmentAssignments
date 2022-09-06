'''
The natural numbers, also called the counting numbers, are the positive whole numbers starting with one.  That is, the first five natural numbers are 1, 2, 3, 4, 5.  It's that simple.

We're going to write a program that creates a list holding the first N natural numbers, where N is given by the user.

So, first you will ask the user for a number, which will be N.  Then, do whatever it takes using loops and append to create a list that holds the first N natural numbers!

Finally, print this list.
'''

'''
Enter the maximum for our list of natural numbers: 10

The first 10 natural numbers are:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

x = int(input("Enter the maximum for our list of natural numbers: "))
print("The first 10 natural numbers are:")
numbers = []
for i in range(1, x + 1):
	numbers.append(i)
print(numbers)

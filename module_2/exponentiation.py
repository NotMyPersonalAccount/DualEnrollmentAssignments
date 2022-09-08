'''
Write a program that asks for a number base, and an exponent.

Then calculate the result of the exponentation without using Python's ** operator, and print it out nicely with a reminder of what math problem you're doing, as show in the example below:
'''

'''
What's the base? 5
What's the exponent? 3
5 to the power of 3 is 125.
'''

x = int(input("What's the base? "))
y = int(input("What's the exponent? "))
print(f"{x} to the power of {y} is {x ** y}")

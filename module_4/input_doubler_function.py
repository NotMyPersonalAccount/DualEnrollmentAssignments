'''
Write a function that takes one argument. 

It should behave like the function input, with two differences:

1.  It should expect to get an int as the input typed in by the user, and return an int.

2.  It should return whatever the user gives as input, but doubled!

 

The argument provided to your function should behave just like the argument provided to input: it should be printed as a helpful message before the program waits for user input.
'''

def input_double(prompt):
	return int(input(prompt)) * 2

print(input_double("Please enter an integer for me to double: "))

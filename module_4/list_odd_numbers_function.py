'''
Write a function that takes one argument, a list.  Assume that the list contains only integers (whole numbers).

The function should return the boolean value True if the list contains even a single odd number, and False if the list contains no odd numbers.

 

So, if for example, if the function is called with the argument [0, 5, 10, 30, 31], it will return True, because it contains one or more odd numbers.

If the function is called with the argument [0, 2, 4, 10, 30], it will return False, because it contains only even numbers.

'''

def list_odd_numbers(list):
	for i in list:
		if i % 2 == 1:
			return True
	return False

print(list_odd_numbers([0, 5, 10, 30, 31]))
print(list_odd_numbers([0, 2, 4, 10, 30]))

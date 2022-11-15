'''
Write a function that takes one argument, a list.

The function should print out each element in the list, one on each line.

 

The function should not return anything!  This is our first time creating a custom function that has side effects, and no return value.
'''

def print_list(list):
	for i in list:
		print(i)

print_list([10, 20, 30])

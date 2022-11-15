'''
Write a function that takes two arguments, a list and an int.

The function should return the element in the first argument at the index of the second argument!

 

So, if the function is given the list [10,20,30] as its first argument and the int 1 as its second argument, it should return 20.
'''

def element(list, i):
	return list[i]

print(element([10, 20, 30], 1))

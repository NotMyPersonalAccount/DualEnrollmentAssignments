'''
Write a function that takes one argument, a list.  Assume that this list can contain any data types!

Return True if the function contains at least one pair of values that are the same.

Return False if the function contains only unique values with no repeats.

 

So, for example, if the function is called with the argument [0, 1, "hello", 3.5], return False, because each of the four list elements is unique.

If the function is called with the argument [0, 1, "hello," 3.5, "hello"], return True, because the value "hello" appears more than one time.
'''

def has_repeat_values(list):
	found = []
	for i in list:
		for j in found:
			if i == j:
				return True
		found.append(i)
	return False

print(has_repeat_values([0, 1, "hello", 3.5]))
print(has_repeat_values([0, 1, "hello", 3.5, "hello"]))

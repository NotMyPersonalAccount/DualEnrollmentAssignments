'''
Start with a list of numbers (you can use ints or floats) assigned to a variable.

Then, print a list equal to the original list, but with each number having been doubled.

Use while loop iteration!
'''

'''
The list is [5, 12, 50, -1].
Doubled, the list is [10, 24, 100, -2].
'''

list = [5, 12, 50, -1]
print(f"The list is {list}")

i = 0
multipliedList = []
while i != len(list):
	multipliedList.append(list[i] * 2)
	i += 1
print(f"Doubled, the list is {multipliedList}")

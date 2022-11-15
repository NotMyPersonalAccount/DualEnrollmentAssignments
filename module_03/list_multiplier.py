'''
Start with a list of numbers (you can use ints or floats) assigned to a variable.  Then, print it and ask the user what number they should each be multiplied by.

Then, print a new list, with each entry having been multiplied by the number the user entered.

Use while loop iteration!  (As a bonus challenge, see if you can do this without a while loop.)

'''

'''
The list is [5, 12, 50, -1].

Enter number to multiply each item by: 10

Here's the multiplied list you ordered: [50, 120, 500, -10]
'''

list = [5, 12, 50, -1]
print(f"The list is {list}")
x = int(input("Enter number to multiply each item by: "))

i = 0
multipliedList = []
while i != len(list):
	multipliedList.append(list[i] * x)
	i += 1
print(f"Here's the multiplied list you ordered: {multipliedList}")

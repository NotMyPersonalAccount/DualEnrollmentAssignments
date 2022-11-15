'''
Assign a list of numbers to a variable, and print it.  Then, ask the user to enter a number.

If the number is in the list, respond with all the indices at which the number appears in the list.

If the number isn't in the list, respond with a message to that effect.
'''

'''
Welcome to ListChecker 5000!
The list is [100, -5, -121, 0, 10, 20, 50, 10]
What number should I check for? 10

That appears at the following indices in the list: [4, 7].
'''

list = [100, -5, -121, 0, 10, 20, 50, 10]
print("Welcome to ListChecker 5000!")
print(f"The list is {list}")
x = int(input("What number should I check for? "))

indices = []
for i in range(len(list)):
	if list[i] == x:
		indices.append(i)
if len(indices) == 0:
	print("That does not appear in the list")
else:
	print(f"That appears at the following indices in the list: {indices}")

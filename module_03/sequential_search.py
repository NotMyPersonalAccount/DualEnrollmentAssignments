'''
Assign a list of numbers to a variable, and print it.  Then, ask the user to enter a number.

If the number is in the list, respond with the index at which the number first appears in the list.

If the number isn't in the list, respond with a message to that effect.
'''


'''
Welcome to ListChecker 5000!
The list is [100, -5, -121, 0, 10, 20, 50, 10]
What number should I check for? 10

That first appears at index 4 in the list.
'''

list = [100, -5, -121, 0, 10, 20, 50, 10]
print("Welcome to ListChecker 5000!")
print(f"The list is {list}")
x = int(input("What number should I check for? "))

found = False
for i in range(len(list)):
	if list[i] == x:
		print(f"That first appears at index {i} in the list.")
		found = True		
		break
if not found:
	print("That does not appear in the list")

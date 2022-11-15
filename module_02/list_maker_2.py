'''
This problem is similar to the last, with one difference: The list can be any length, and the user will decide the length.

First, ask the user for a length of list to remember.

Then, repeatedly ask the user for strings to remember, adding each one to the list.

When the list has reached the desired length, stop asking for new strings.

Then, print out each item in the list with a helpful message.
'''

'''
How many items should I remember? 5
What's the first item? Bread
What's the next item? Tofu
What's the next item? Coconut 
What's the next item? Oranges
What's the next item? Honey

The items are:
Bread
Tofu
Coconut
Oranges
Honey
'''

i = input("How many items should I remember? ")
items = []
for j in range(int(i)):
    description = "first" if j == 0 else "next"
    items.append(input(f"What's the {description} item "))
print("The items are:")    
for k in items:
    print(k)

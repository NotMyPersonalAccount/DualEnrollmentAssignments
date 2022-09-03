'''
Ask the user for three strings to remember in a list.

As the user gives each item, add that item to a list.

Then, print out each item in the list with a helpful message.
'''

'''
What's the first item? Bread
What's the second item? Tofu
What's the third item? Coconut

The items are:
Bread
Tofu
Coconut
'''

items = []
numbers = ["first", "second", "third"]
for n in numbers:
    items.append(input(f"What's the {n} item? "))
print("The items are:")
for i in items:
    print(i)

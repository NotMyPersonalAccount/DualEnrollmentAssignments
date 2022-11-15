'''
Write a program that defines a dictionary with at least three key-value pairs.  Then, do the following things in order:

Print the dictionary.
Print a single value from the dictionary (remember, the value is the data stored in the box.  The key is the name of the box.)
Remove a key-value pair from the dictionary.
Print the dictionary again.
Add one or more key-value pairs to the dictionary.
Print the dictionary again.
That's it! Make sure that the dictionary holds what you expect at each step it's printed.
'''

dict = {
    "pig": 1,
    "cow": 2,
    "sheep": 3
}
print(dict)
print(dict["pig"])
del dict["cow"]
print(dict)
dict["chicken"] = 4
print(dict)

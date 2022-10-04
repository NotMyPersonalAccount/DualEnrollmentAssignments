'''
rite a function that takes two arguments, both of which are assumed to be dictionaries.

The function should return a dictionary that contains all the key-value pairs contained in both dictionaries!  So, for example, if it's given the following two arguments:

{'a': 1, 'b': 2}

and

{'c': 3, 'd': 4, 'e': 5}

it should return the dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.

 

Note: If there are any keys that are in both dictionaries given as arguments, make sure that the dictionary given as the FIRST argument is the one whose key-value pair appears in the returned dictionary!  So, for example, if the function is given the following two arguments:

{'a': 1, 'b': 2}

and

{'b': 999, 'c': 3, 'd': 4, 'e': 5}

it should return the dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.

 

Reminder: You can get a list of all the keys in a dictionary by giving it as an argument to the built-in Python function list. Ask if you have questions about this.
'''

def merge(dict1, dict2):
    for key, value in dict2.items():
        if not key in dict1:
            dict1[key] = value
    return dict1

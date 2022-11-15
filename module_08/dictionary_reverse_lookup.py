'''
Write a function that takes two arguments: A dictionary, and a value of any kind.

The function should return all the keys in the dictionary whose value is the second argument! This is like a reverse phone book lookup, where instead of giving a name and getting a number, you give a number and get a name.

Since there could be multiple keys whose value is the second argument, return ALL keys whose value is the second argument, in a list.

So, for example, if the function was given the following dictionary:

{'animal': cat, 'word' 'cat', 'color': 'blue'}

and the value 'blue'

It would return a list containing only one element: ['color']

 

If the function was given the same dictionary:

{'animal': cat, 'word' 'cat', 'color': 'blue'}

and the value 'cat'

It would return a list containing two elements: ['animal', 'word']
'''

def lookup_keys(dict, value):
    keys = []
    for key, v in dict.items():
        if  v == value:
            keys.append(key)
    return keys

print(lookup_keys({"a": 1, "b": 1, "c": 2}, 1))

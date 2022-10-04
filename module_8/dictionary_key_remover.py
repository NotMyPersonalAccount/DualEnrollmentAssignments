'''
Write a function that takes two arguments: The first should be assumed to be a dictionary, and the second assumed to be a list of keys that appear in the dictionary.

Remove all key-value pairs in the dictionary whose key appears in the list of keys.  Then return the dictionary.

 

So, for example, if the function is given the following two arguments:

The dictionary {'Oakland': 425000, 'Berkeley': 121000, 'San Francisco': 875000}

and the list ['Oakland', 'San Francisco']

It should remove all key-value pairs whose key is in the list, and return the dictionary, modified so that it contains only {'Berkeley': 121000}
'''

def remove_key(dict, keys):
    for key in keys:
        del dict[key]
    return dict

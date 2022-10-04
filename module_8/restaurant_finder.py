'''
Write a function that takes three arguments: A list of dictionaries, a string, and another string.

The first string should be interpreted as a key.  The second string should be interpreted as a value.

The function should return a list of all dictionaries that contain the key-value pair given as the second and third arguments!

So, for example, if the list of dictionaries given as the first argument is as follows:

[

{

   'name': 'Lake Merritt Pizza',

   'type': 'Pizza,

   'zip_code': 94611

},

{

   'name': 'Fat Slice',

   'type': 'Pizza,

   'zip_code': 94705

},

{

   'name': 'Long Life Veggie House,

   'type': 'Chinese',

   'zip_code': 94705

}

]

And the first string (the key) is 'type', and the second string (the value) is 'Pizza', the function will return a list containing the first two restaurants, in dictionary form.
'''

def find_restaurant(restaurants, key, value):
    found = []
    for restaurant in restaurants:
        if restaurant[key] == value:
            found.append(restaurant)
    return found

'''
Create a dictionary with at least five key-value pairs.  Then, iterate over the dictionary's keys, printing out one key-value pair on each line!

To do this, you'll pass the dictionary into the built-in Python function list, which gives you a list of all the keys in the dictionary.

Note: There are easier ways to iterate over a dictionary, but we're going to learn this one first because it teaches good programming fundamentals.

So, if the dictionary were {'name': 'Oakland', 'population': 425,000, 'type': 'City', 'founded':1772, 'mayor': 'Libby Schaaf'}

The program would print out the following:

name: Oakland
population: 425,000
type: City
founded: 1772
mayor: Libby Schaaf
'''

dict = {"pig": 1, "cow": 2, "sheep": 3, "chicken": 4, "goat": 5}
for key, value in dict.items():
    print(f"{key}: {value}")

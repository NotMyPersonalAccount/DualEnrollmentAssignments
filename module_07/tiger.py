'''
Part One:

Create a Tiger class, whose constructor takes one arguments, which I'll call starting_name.

Every tiger should have one instance variables created upon initialization, called name, taken from the argument to the constructor.

Put this class definition in its own file!

 

Part Two:

In main.py, import the Tiger class.

Then, create a data structure that holds specific name information for at least five tigers.

Finally, iterate over this data structure, instantiating all five tigers, and putting them into a list.

Make sure the instances of tigers are all saved into that list!
'''

class Tiger:
    def __init__(self, starting_name, starting_stripes):
        self.starting_name = starting_name
        self.starting_stripes = starting_stripes

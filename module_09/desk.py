'''
Write a definition of class Desk, which has three instance variables: height, length, width, and contents.

height, length, and width should be assumed to be numbers.  Floats or ints are both okay.

contents should be a list.  It's intended to list all the things that are contained in the desk (say, pencils, papers, etc.).

 

An instance of Desk should be initialized with height, length, and width given as arguments to the constructor.  contents should always initially be an empty list!

 

All desks should have two instance methods: putindesk and volume.

volume is a function that takes no arguments and returns the height * length * width, as we've done before.

putindesk is a function that takes one argument, an item of any data type that should be appended to the list contents.

 

You don't have to make any instance method to remove an item from the desk's contents.  If you're up for a challenge, it's a good stretch goal, but that goes beyond regular preparation for the midterm.
'''

class Desk:
    contents = []

    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width
    def putindesk(self, item):
        self.contents.append(item)
    def volume(self):
        return self.height * self.length * self.width

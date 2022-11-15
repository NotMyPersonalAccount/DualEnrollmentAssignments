'''
Create a class Square that's similar to the Circle class example!  Instead of the instance method circumference, name the method perimeter.

Instead of radius, call the instance variable side_length and do the calculations of perimeter and area appropriately.

Then, test your class by creating two Square instances, each with a different side_length, and test every one of each Square's methods, making sure you get what you expect.
'''
class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    def perimeter(self):
        return self.side_length * 4
    def area(self):
        return self.side_length ** 2

from math import pi, sqrt

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2 * pi * self.radius
    def area(self):
        return pi * self.radius ** 2
    '''
    Using the code for the Circle class example, and your new Square class (written in the previous problem), write a Circle instance method called transform_to_square whose return value is a new instance of the Square class!

    The new Square should be created to have the same area as the Circle! This will require a little bit of algebra and geometry.

    Then, create a Circle, get its self-reported area, transform it to a Square, and make sure the Square's self-reported area is very similar.
    '''
    def transform_to_square(self):
        return Square(sqrt(self.area()))

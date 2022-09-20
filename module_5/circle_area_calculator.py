'''
Ask the user for the radius of a circle.

Then, print a helpful message giving the area of a circle.

In this exercise, instead of approximating pi as 3.14, use the pi found in the math module of the standard library!
'''

'''
Enter the radius of the circle: 2.6

The radius of the circle is 21.237166338267002.
'''

from math import pi

radius = float(input("Enter the radius of the circle: "))
print(f"The radius of the circle is {pi * radius ** 2}")

from random import randint

'''
Create a class called Restaurant that does nothing special.  That's it! Make sure you that you can "create an instance of," or instantiate, the Restaurant class.
'''
class Restaurant:
    '''
    Give it an __init__ function that takes three arguments in addition to self, which are the restaurant's type, name, and ZIP code.  Make the __init__ function assign the type, name, and ZIP code to instance variables called type, name, and ZIP.

    Make sure that you can instantiate Restaurants with any type, name, and ZIP code, and that these are properly placed into instance variables.
    '''
    def __init__(self, restaurant_type, name, zip_code, menu):
        self.restaurant_type = restaurant_type
        self.name = name
        self.zip_code = zip_code
        self.menu = menu
    '''
    Now, create an instance method called describe that makes any instance of Restaurant print a helpful message.  The message must give its name, what type of food it serves, and what ZIP code it's located in.

    Make sure that you can instantiate multiple Restaurants with different types, names, and ZIPs, and that each one describes itself correctly!
    '''
    def describe(self):
        menu_items = list(self.menu)
        print(f"{self.name} is a restaurant that serves {self.restaurant_type} at zip code {self.zip_code} that serves {menu_items[randint(0, len(menu_items) - 1)]}")

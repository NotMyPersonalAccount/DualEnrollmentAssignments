'''
Ask the user at least three questions about themself then repeat what you've learned using a single Python print statement with a format string given as argument.
'''

'''
What's your name? Dracula
How old are you? 846
What's your favorite food? blood
Hi, Dracula! You're 846 years old and your favorite food is blood.
'''

name = input("What's your name? ")
age = input("How old are you?")
food = input("What's your favorite food? ")
print(f"Hi, {name}! You're {age} years old and your favorite food is {food}")

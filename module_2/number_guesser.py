'''
Choose a secret number and assign it to a variable in your program.

Then, when the program runs, ask the user for a guess at the number.

Print an appropriate response if the user's guess is higher than, lower than, or equal to the secret number.

The program can then finish.

Three example runs of the program are shown below.  Let's say the secret number held in a variable in the program is 50.
'''

'''
What's the secret number? 1
The secret number is higher than that!
'''

'''
What's the secret number? 38831
The secret number is lower than that!
'''

'''
What's the secret number? 50
YOU GOT IT!
'''

import random

number = random.randint(0, 100)
guess = int(input("What's the secret number? "))
if guess == number:
    print("YOU GOT IT!")
elif guess < number:
    print("The secret number is higher than that")
else:
    print("The secret number is lower than that")


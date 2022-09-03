'''
This is like Number Guesser 1, except now you should keep running until the user correctly guesses the number!

One example run of the program is shown below.  Let's say the secret number held in a variable in the program is 7.
'''

'''
What's the secret number? 5
The secret number is higher than that!
What's the secret number? 10
The secret number is lower than that!
What's the secret number? 7
YOU GOT IT!
'''

import random

number = random.randint(0, 100)
while True:
    guess = int(input("What's the secret number? "))
    if guess == number:
        print("YOU GOT IT!")
        break
    elif guess < number:
        print("The secret number is higher than that")
    else:
        print("The secret number is lower than that")

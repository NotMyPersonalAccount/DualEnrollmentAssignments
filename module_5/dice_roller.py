'''
Write a program that helpfully rolls simulated dice, using the random module in the standard library.

The program should ask for a number of dice to roll, and the number of sides per die.  Then, simulate the roll and produce the number that comes up.  Assume these are fair dice with an equal chance per side.
'''

'''
Enter the number of dice to roll: 2
Enter the number of sides per die: 6 

You rolled (2) 6-sided dice and got: 9.
'''

'''
For an optional challenge, and a more useful program, make the program loop, so you can roll dice over and over by hitting enter.
'''

from random import randint

dice = int(input("Enter the number of dice to roll: "))
sides = int(input("Enter the number of sides per die: "))

while True:
	total = 0
	for _ in range(dice):
		total += randint(1, sides)
		input(f"You rolled ({dice}) {sides}-sided dice and got: {total}")

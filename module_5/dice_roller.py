from random import randint

dice = int(input("Enter the number of dice to roll: "))
sides = int(input("Enter the number of sides per die: "))

total = 0
for _ in range(dice):
	total += randint(1, sides)
print(f"You rolled ({dice}) {sides}-sided dice and got: {total}")

'''
In this exercise we're going to practice using the statistics module in the Python standard library by calculating the mean, median, and mode of a list of floats.

So, the first thing needed is a list of floats!  You can get this list in any way you choose:  You can ask the user to enter them one by one, or generate them randomly (using the random module), or by just creating a list in the program.

Next, use the statistics module to print the mean, median, and mode of the list, with a helpful message.
'''

'''
Enter the next number (or leave blank to end the list): 5.1
Enter the next number (or leave blank to end the list): 5.1
Enter the next number (or leave blank to end the list): 7.8
Enter the next number (or leave blank to end the list): 3
Enter the next number (or leave blank to end the list): 2
Enter the next number (or leave blank to end the list):

The mean of these numbers is 4.6, the median is 5.1, and the mode is 5.1.
'''

from statistics import mean, median, mode

numbers = []
while True:
	number = input("Enter the next number (or leave blank to end the list): ")
	if number == "":
		break
	numbers.append(int(number))
print(f"The mean of these numbers is {mean(numbers)}, the median is {median(numbers)}, and the mode is {mode(numbers)}")

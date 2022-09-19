from statistics import mean, median, mode

numbers = []
while True:
	number = input("Enter the next number (or leave blank to end the list): ")
	if number == "":
		break
	numbers.append(int(number))
print(f"The mean of these numbers is {mean(numbers)}, the median is {median(numbers)}, and the mode is {mode(numbers)}")

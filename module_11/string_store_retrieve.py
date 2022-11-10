'''
Write a program that creates an interactive menu allowing the user to store a string in a file, and retrieve that string from the file.  Since the string will be written to a file, this means that it will be remembered even if the program quits and restarts!

Example output is shown below for two different runs of the program.  User input is shown in green as always.
'''

'''
Welcome to StringStore!

Would you like to (R)etrieve the string, (S)tore a new one, or (Q)uit? s
What's the new string you'd like to store? Veggie Bun
Ok, string has been stored.
Would you like to (R)etrieve the string, (S)tore a new one, or (Q)uit? r
The stored string is 'Veggie Bun'.
Would you like to (R)etrieve the string, (S)tore a new one, or (Q)uit? q
'''

'''
And then, after quitting and restarting the program, the program will remember the most recent string, because it was stored in a file!
'''

'''
Welcome to StringStore!

Would you like to (R)etrieve the string, (S)tore a new one, or (Q)uit? r 
The stored string is 'Veggie Bun'.
Would you like to (R)etrieve the string, (S)tore a new one, or (Q)uit? q
'''

'''
Note: You can assume that the user will store a string before they try to retrieve it on the very first time the program is run.

Final note: You can call the filename in which the string is stored anything you like.
'''

print("Welcome to StringStore!")

file = open("string_store", "r+")
while True:
	action = input("Would you like to (R)etrieve the string, (S)tore a new one, or (Q)uit? ")
	if action == "q":
		break
	if action == "s":
		value = input("What's the new string you'd like to store? ")
		file.write(value)
		print("Ok, string has been stored.")
	elif action == "r":
		print(f"The stored string is '{file.read()}'.")
file.flush()
file.close()
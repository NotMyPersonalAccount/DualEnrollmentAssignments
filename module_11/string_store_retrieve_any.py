'''
Write a program that creates an interactive menu allowing the user to enter a filename, assumed to be a valid filename containing a single string, and retrieve and print the string in that file.

Example output is shown below, assuming that there are three files available, called somefile, anotherfile, and athirdfile.  You can call your test files whatever you'd like and have as many as you like!
'''

'''
Welcome to StringRetriever!

Would you like to (R)etrieve the string in a file or (Q)uit? r
What's the file name? anotherfile
That contains the string 'Chicken'.
Would you like to (R)etrieve the string in a file or (Q)uit? r
What's the file name? athirdfile
That contains the string 'foo'.
Would you like to (R)etrieve the string in a file or (Q)uit? r
What's the file name? somefile
That contains the string 'blah'.
Would you like to (R)etrieve the string in a file or (Q)uit? q
'''

print("Welcome to StringRetriever!")
while True:
	action = input("Would you like to (R)etrieve the string in a file or (Q)uit? ")
	if action == "q":
		break
	if action == "r":
		filename = input("What's the file name? ")
		file = open(filename, "r")
		print(f"That contains the string '{file.read()}'.")
		file.close()
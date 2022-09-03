'''
First, print a custom welcome message to your calculator.  This welcome should only be printed once, at program start.

Ask the user for a first number, a second number, and a math operation.  Support at least the four basic arithmetic operations addition, subtraction, multiplication, and division.

Then, apply the math operation to the two numbers and print the result. 

Then do it again!  Never stop asking for another calculation to do.

Use input, print, and float!
'''

'''
Welcome to Michael's HyperCalc™ Version 1 Alpha!

Enter the first number: 10
Enter the second number: 5
Enter the operation (please enter one of +, -, *, /): /
2.0
Enter the first number: 2
Enter the second number: 4
Enter the operation (please enter one of +, -, *, /): *
8.0

(And on and on until the program is stopped.)
'''

print("Welcome to Linus Torvalds' HyperCalc™ Version 1 Alpha!")

def calculate(first, second, operator):
    match operator:
        case "+":
            return first+second
        case "-":
            return first-second
        case "*":
            return first*second
        case "/":
            return first/second

while True:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    operator = input("Enter the operation (please enter one of +, -, *, /)")    
    print(calculate(first, second, operator))

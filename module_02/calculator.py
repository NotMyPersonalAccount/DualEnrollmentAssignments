'''
Ask the user for a first number, a second number, and a math operation.  Support at least the four basic arithmetic operations addition, subtraction, multiplication, and division.

Then, apply the math operation to the two numbers and print the result.  The program can then exit.

Use input, print, and float!
'''

'''
Enter the first number: 10
Enter the second number: 5
Enter the operation (please enter one of +, -, *, /): /
2.0
'''

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operator = input("Enter the operation (please enter one of +, -, *, /)")

def calculate():
    match operator:
        case "+":
            return first+second
        case "-":
            return first-second
        case "*":
            return first*second
        case "/":
            return first/second

print(calculate())

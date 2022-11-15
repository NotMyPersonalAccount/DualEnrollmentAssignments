'''
Create a class called Stack that implements a stack, the type of data store we discussed in class Tuesday Oct. 26.

Every instance of Stack should have two instance methods:

push, which takes one argument, and sticks that argument on top of the stack.

pop, which takes zero arguments, removes the element on top of the stack from that stack, and returns it.

If the stack is popped when it's empty, print a helpful message like 'Stack is empty' and return nothing!

Use a regular Python list to actually hold the items!

 

Python has built-in methods that will make this easy, but the challenge is to build this using only very basic list operations.  So here are the limitations of what you can use:

You can append to lists.
You can use del to delete items from lists.
You can use any control flow statements, including loops (like while), conditionals (like if, elif, else).
You can use the len function.
 

Basically, I don't want you using Python's very helpful built-in functions like list.pop() that will do much of the work for you.  Think about how to make this from near-scratch!
'''
class Stack:
    items = []

    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
            return
        item = self.items[-1]
        del self.items[-1]
        return item

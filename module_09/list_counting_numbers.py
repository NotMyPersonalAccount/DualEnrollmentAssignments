'''
Write a function that takes a single argument, which I'll call n.  Assume that n is an int greater than or equal to 1.

The function should return a list of length n, where each element is an int, starting at 1 and counting up by 1 each time.

So, for example, if the function is given the argument 5, it should return the following list:

[1, 2, 3, 4, 5]

For another example, if the function is given the argument 3, it should return the following list:

[1, 2, 3]

And, of course, if the function is given the argument 1, it should return the following list:

[1]

 

Helpful reminder:  Don't just build the list and forget to return it! Remember to return the list after you've made it in the function.
'''

def counting_numbers(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers

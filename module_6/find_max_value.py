'''
Write a function that takes a single argument, a list of floats.  It should return the largest number in the list.

If there's a tie for largest number, no problem; just return that largest number.

Use the classic algorithm we discussed in class or make up your own!

For example, if the function is given the argument [-5.0, 6.1, 100.123, 37.5], it should return 100.123.
'''

def find_max(list):
    max = list[0]
    for i in range(1, len(max)):
        if list[i] > max:
            max = list[i]
    return max

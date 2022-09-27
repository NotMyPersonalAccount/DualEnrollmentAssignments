'''
Write a function that takes a single argument, a list of numbers.  You can choose whether to support ints or floats.

Have the function return a list of the same numbers, sorted!  That is, the first index should contain the smallest number, and the last index should contain the largest number.

For example, if the function is given the list [0, -1, 1, -5, 10] it should return [-5, -1, 0, 1, 10].

Your function should handle duplicated values in the argument list! For example, if the function is given the list [10, 10, 10, 1], it should return [1, 10, 10, 10].

 

Note:  For this exercise you can choose whether to modify the list given as argument and return that, or create an entirely new sorted list and return that.
'''

def sort(list):
    sorted = []
    while len(list) > 0:
        min_index = 0
        for index in range(len(list)):
            if list[index] < list[min_index]:
                min_index = index
        min = list.pop(min_index)
        sorted.append(min)
    return sorted

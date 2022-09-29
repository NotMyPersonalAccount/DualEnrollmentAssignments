'''
Write a function that takes a single argument, a list of numbers.  You can choose whether to support ints or floats.

Have the function return a list of the same numbers, sorted!  That is, the first index should contain the smallest number, and the last index should contain the largest number.

For example, if the function is given the list [0, -1, 1, -5, 10] it should return [-5, -1, 0, 1, 10].

Your function should handle duplicated values in the argument list! For example, if the function is given the list [10, 10, 10, 1], it should return [1, 10, 10, 10].

 

Note:  For this exercise you can choose whether to modify the list given as argument and return that, or create an entirely new sorted list and return that.
'''

def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i + 1
        for j in range(i + 1, len(list)):
            print(i, j)
            if list[min_index] > list[j]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp
    return list

def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list

from random import randint

def bogo_sort(list):
    while True:
        for i in range(len(list)):
            key = randint(0, len(list) - 1)
            temp = list[i]
            list[i] = list[key]
            list[key] = temp
        for i in range(1, len(list)):
            if list[i - 1] > list[i]:
                break
        else:
            break
    return list

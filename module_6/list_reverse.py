'''
Write a function that takes a single argument, a list of any values.  Those values can even be mixed in the same list, so for example the argument list could contain both ints and strings.

Return the argument list, reversed.

For example, if the function is given the argument [1, 2, 3, "all you can eat sushi"], it should return ["all you can eat sushi", 3, 2, 1]

Note: You can modify the list given as argument and return that, or create a new list of the reversed values and return that.  Either is fine.
'''

def reverse(list):
    for i in range(int(len(list) / 2)):
        temp = list[i]
        list[i] = list[len(list) - i - 1]
        list[len(list) - i - 1] = temp
    return list

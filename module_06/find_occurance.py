'''
Write a function that takes two arguments, a list of ints and a single int.  We'll call the list argument l and the single int n.

The function returns an int representing the index in l at which n appears, or -1 if n does not appear anywhere in l!

For example, if the function is given the arguments [5, 10, 15, 20] and 10, it should return 1 because that's the index in l at which n (in this case, 10) is present.

For another example, if the function is given the arguments [5, 10, 15, 20] and 3, it should return -1 because -1 doesn't appear anywhere in l!
'''

def find_occurance(list, x):
    for i in range(len(list)):
        if x == list[i]:
            return i
    return -1

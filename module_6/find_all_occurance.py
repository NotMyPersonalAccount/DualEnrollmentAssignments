'''
Write a function that takes two arguments, a list of ints and a single int.  We'll call the list argument l and the single int n.

The function returns a list, whose elements are ints. Each int in the returned list represents an index in l at which n appears.

For example, if the function is given the arguments [5, 10, 15, 20] and 10, it should return [1] because that's the only index in l at which n (in this case, 10) is present.

For another example, if the function is given the arguments [10, 10, 200, 10] and 10, it should return [0, 1, 3] because those are the indices where 10 appears in l!

For another example, if the function is given the arguments [5, 10, 15, 20] and 3, it should return [], because 3 doesn't appear anywhere in l!
'''

def find_all_occurance(list, x):
    occurances = []
    for i in range(len(list)):
        if x == list[i]:
            occurances.append(i)
    return occurances

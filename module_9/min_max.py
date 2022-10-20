'''
Write a function that takes two arguments:

The first, which I'll call numlist, is assumed to be a list of integers or other numbers that can be compared with < and >.  Assume that numlist has length at least 1.
The second, which I'll call maxormin, is assumed to be either the string "max" or the string "min".
Your function should always return a single number that's in numlist.  What it returns is decided as follows:

If str is "max", then your function should return the highest number in numlist.

If str is "min", then your function should return the lowest number in numlist.

 

Hint: Reviewing the practice problem on the FindMax algorithm will be helpful for this one!
'''

def min_max(numlist, maxormin):
    result = numlist[0]
    for i in range(1, len(numlist)):
        j = numlist[i]
        if (result > j and maxormin == "min") or (result < j and maxormin == "max"):
            result = j
    return result

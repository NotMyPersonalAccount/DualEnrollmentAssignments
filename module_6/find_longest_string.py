'''
Write a function that takes a single argument, a list of strings.  It should return the longest string in the list.

If there's a tie for longest string, return the first string of that longest length!  That is, return the string of longest length with the lowest index in the list.

For example, if the function is given the argument ['a', 'cat', 'b', 'dog', 'c'], it should return 'cat' because that's the first string of length 3.

Note: Assume that the list you're given contains at least one string! You don't have to worry about the case in which your function is given an argument that's an empty list.
'''

def find_longest_string(list):
    longest = list[0]
    for i in range(1, len(list)):
        if len(list[i]) > len(longest):
            longest = list[i]
    return longest

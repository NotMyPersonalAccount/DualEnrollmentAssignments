'''
For example, if the function is given the argument ['a', 'cat', 'b', 'dog', 'c'], it should return the list ['cat', 'dog'] because those are the two strings of length 3, the longest length.

As another example, if the function is given the argument ['a', 'ab', 'abc', 'abcd'] it should return the list ['abcd'], containing only one element, because there's only one string with the longest length.

Note: Assume that the list you're given contains at least one string! You don't have to worry about the case in which your function is given an argument that's an empty list.
'''

def find_all_longest_string(list):
    longest = [list[0]]
    for i in range(1, len(list)):
        if len(list[i]) > len(longest[0]):
            longest = [list[i]]
        elif len(list[i]) == len(longest[0]):
            longest.append(list[i])
    return longest

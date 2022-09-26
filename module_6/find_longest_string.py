def find_longest_string(list):
    longest = list[0]
    for i in range(1, len(list)):
        if len(list[i]) > len(longest):
            longest = list[i]
    return longest

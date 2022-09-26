def find_all_longest_string(list):
    longest = [list[0]]
    for i in range(1, len(list)):
        if len(list[i]) > len(longest[0]):
            longest = [list[i]]
        elif len(list[i]) == len(longest[0]):
            longest.append(list[i])
    return longest
print(find_all_longest_string(["ab", "ccc", "ffdffd", "123456789", "abcdefghi"]))

def find_max(list):
    max = list[0]
    for i in range(1, len(max)):
        if list[i] > max:
            max = list[i]
    return max

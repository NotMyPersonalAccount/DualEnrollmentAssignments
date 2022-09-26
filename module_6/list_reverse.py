def reverse(list):
    for i in range(int(len(list) / 2)):
        temp = list[i]
        list[i] = list[len(list) - i - 1]
        list[len(list) - i - 1] = temp
    return list

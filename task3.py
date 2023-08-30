encoded_lists = [
    [1, 2, 3, 4, 6],
    [5, 7, 8, 9, 15],
    [12, 14, 16, 18],
    [10, 11, 12, 13, 16, 17, 18, 20]]


def explode_chains():
    for list in encoded_lists:
        n = len(list)
        i = 0
        while (i < n - 2):
            if (list[i + 1] - list[i] == 1 and list[i + 2] - list[i + 1] == 1):
                list.pop(i)
                list.pop(i)
                list.pop(i)
                n = n - 3
            i = i + 1
        print(list)


explode_chains()

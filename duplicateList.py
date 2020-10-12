def removeDuplicate(x):
    return list(dict.fromkeys(x))


obj_list = removeDuplicate([1, 2, 4, 6, 2, 1, 4, 5, 7, 8, 6])

print(obj_list)

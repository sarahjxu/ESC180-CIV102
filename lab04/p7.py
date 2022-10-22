def duplicates(list0):
    i = 0
    for i in range(len(list0)):
        if i+1 < len(list0):
            if list0[i] == list0[i+1]:
                return True
    return False

list0 = [1, 2, 3, 4, 5]
print(duplicates(list0))
list1 = [1, 2, 2, 3, 4, 5, 5]
print(duplicates(list1))
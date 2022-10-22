def lists_are_the_same(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

list1 = [1, 2, 3]
list2 = [8, 3, 5]
print(lists_are_the_same(list1, list2))

list3 = [1, 2, 3]
list4 = [1, 2, 3]
print(lists_are_the_same(list3, list4))

list5 = [1]
list6 = [4, 7, 6]
print(lists_are_the_same(list5, list6))
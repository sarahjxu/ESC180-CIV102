def list1_start_with_list2(list1, list2):
    wrong = 0
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            wrong += 1
    if len(list1) >= len(list2) and wrong == 0:
        return True
    return False


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 3]
print(list1_start_with_list2(list1, list2))

list3 = [1, 2, 3, 4, 5, 6, 7, 8]
list4 = [1, 2, 3, 4]
print(list1_start_with_list2(list3, list4))
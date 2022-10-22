def match_pattern(list1, list2):
    i = 0
    j = 0
    for i in range(len(list1)):
        if list1[i] == list2[0]:
            if i + len(list2) >= len(list1):
                break
            for k in range(i, i + len(list2)):
                if list1[k] != list2[j]:
                    break
                j+=1
            return True
        j = 0
    return False

list1 = [1, 2, 4, 3, 4, 5, 6, 7, 8]
list2 = [4, 5, 6, 7]
print(match_pattern(list1, list2))
list3 = [4, 10, 2, 3, 50, 100]
list4 = [2, 3, 50]
print(match_pattern(list3, list4))
list5 = [1, 2, 4, 3, 4, 5, 6, 7, 8]
list6 = [4, 5, 6, 7, 8, 9, 10, 11]
print(match_pattern(list5, list6))
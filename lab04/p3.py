def list_to_str(lis):
    s = '\'['
    i = 0
    for i in range(len(lis)):
        s += str(lis[i])
        if i < len(lis) - 1:
            s += ', '
        i+=1
    return s + ']\''

lis = [45, 7, 8, 5]
print(list_to_str(lis))
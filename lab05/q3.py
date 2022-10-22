def lookup(L, num):
    for i in range(len(L)):
        for j in range(len(L[0]) - 1):
            if L[i][j+1] == num:
                return L[i][j]
    return None

L = [["CIV", 92],
     ["180", 98],
     ["103", 99],
     ["194", 95]]

print(lookup(L, 99))
square_num = 4
print((square_num-1)%3)


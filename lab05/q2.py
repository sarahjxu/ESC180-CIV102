def get_nums(L):
    L1 = ["", "", "", ""]
    for i in range(len(L)):
        L1[i] = L[i][1]
    print(L1)

L = [["CIV", 92],
     ["180", 98],
     ["103", 99],
     ["194", 95]]

get_nums(L)
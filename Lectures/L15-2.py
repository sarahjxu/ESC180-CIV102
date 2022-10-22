L = [1, 2, [3, 4], 5]

L[0]
L[2]
L[2][1]

M = [[1, 2, 3, 4],      #6
     [1, 0, 1, 0],      #7
     [2, 2, 3, 5]]      #8
                        #9
M[1]
M[2][1]

v = [6, 7, 8, 9]

for row in M:
    print(row)

for col_i in range(len(M[0])):
    for row_i in range(len(M)):
        print(str(M[row_i][col_i]) + " ", end = "")
    print("")

def Mult_M_v(M, v):
    '''Multiply matrix M by vector v'''
    res = []
    for row_i in range(len(M)):
        dot_pr = 0
        for col_i in range(len(M[0])):
            dot_pr += M[row_i][col_i] * v[col_i]
        res.append(dot_pr)
    return res

print(Mult_M_v(M, v))

L = [[[[]]]]
len(L) # 1
L[0]
L[0][0]
L[0][0][0]
L[0][0][0][0] # DNE
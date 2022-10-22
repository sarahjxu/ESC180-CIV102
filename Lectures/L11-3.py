L = [5, 6, 7]

def add(a, b):
    return a + b

L = [1, [4, 5], add]

L[0]
L[1]
L[2](5, 6) # functions like add!

print(L[0], L[1], L[2](5, 6))

L[1][0]
L[1][1]

[5, 6][1] # list, first element is 6

print(L[1][0], L[1][1], [5, 6][1])

# append
L = [5, 6, 7]
L.append(10)
print(L)

# slicing
L = [5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16, 17, 18]
L[1:5] # starting from index 1, up to but not including index 5
L[1:7:2]
L[1::7]
print(L[1:5], L[1:7:2], L[1::7])

# using range
res = []
for i in range(1, 7, 2):
    res.append(L[i])
print(res)
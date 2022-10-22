res = 0
for n in range(1001):
    neg = (-1)**n
    div = 2*n+1
    res = res + neg/div
print(res*4)
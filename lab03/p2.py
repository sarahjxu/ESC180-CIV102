res = 0
n = 0
while n < 1001:
    neg = (-1)**n
    div = 2*n+1
    res = res + neg/div
    n += 1
print(res*4)
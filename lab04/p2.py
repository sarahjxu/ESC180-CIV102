def count_evens(L):
    s = 0
    for num in L:
        if num % 2 == 0:
            s += 1
    return s

L = [5, 6, 7, 8, 9, 10]
l = count_evens(L)
print(l)
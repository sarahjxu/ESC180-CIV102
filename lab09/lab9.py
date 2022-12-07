def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return power(x, n-1)*power(x, 1)

# print(power(7, 3))

def interleave(L1, L2):
    if len(L1) == 1:
        return [L1[0], L2[0]]
    else:
        return [L1[0], L2[0]] + interleave(L1[1:len(L1)], L2[1:len(L2)])

# print(interleave([5, 6, 10], [7, 8, 11]))

def previous_elem_bad(L):
    if len(L) == 1:
        return L
    else:
        return previous_elem(L[1:]) + [L[0]]
# parameter that adds index --> no slicing

def previous_elem(L, n):
    if n == 0:
        return L[0]
    else:
        return previous_elem(L[n-1], n-1) + [L[0]]

def reverse_rec(L):
    return previous_elem(L, len(L))

print(reverse_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# def zigzag(L):
#     if len(L) == 0:
#         print("")
#     elif len(L) == 1:
#         print(L[0], end = " ")
#     else:
#         print(L[len(L)//2], L[len(L)//2-1], end = " ")
#         print("hi", len(L)//2)
#         zigzag(L[len(L)//2+1:len(L)//2-1])

# 2, 1, 3, 0, 4

def zigzag1(L):
    if len(L) == 0:
        print("")
    elif len(L) == 1:
        print(L[0], end = " ")
    else:
        print(L[0], L[-1], end = " ")
        zigzag1(L[1:-1])

# zigzag([1, 2, 3, 4, 5])
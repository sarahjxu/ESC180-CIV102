# Fermat's Last Theorem:
# i**p + j**p = l**p has no integer solutions for p > 2

# dovetailing
# for n = 1
#       consider all i in 1...n, all j in 1...n and all k in 1..n
# for n = 2
# do the same
# for n = 3
# do the same
# wasteful but doable

def fermat(p):
    n = 1
    while True:
        for i in range(1, n+1):
            for j in range(1, n+1):
                for k in range(1, n+1):
                    if i**p + j**p == k**p:
                        return i, j, k
        n += 1
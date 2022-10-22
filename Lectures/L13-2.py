# Given a list of L integers, 1, 2, ... n (in some order) with the integer k missing
# want to find k

# [1, 5, 4, 3]
# answer is k = 2, 2 is missing
# puzzle: make this go fast!

# [1, 2, 4]
# largest number missing is 3, if it was [3, 1, 2] with 4 missing...doesn't make sense!

def missing_k_slow(L):
    for k in range(1, len(L) + 1):
        if k not in L:
            return k

def missing_k_fast(L):
    sorted_L = sorted(L) #L.sort() changes the original L
    # how long does it take to sort the list? very fast
    for i in range(1, len(L)):
        if sorted_L[i] - sorted_L[i-1] == 2:
            return L[i-1] + 1

# sorting algorithms

# [5, 1, 10, 50, 25, 12]

# selection sort
# start with a list in arbitrary order
# find the largest element of the list and swap it with whatever element is at the end
# find the largest element in the sublist not including the last element, and swap it with the element at the end of the sublist
# find the largest element in the sublist not including the sorted elements and swap it with the element at the end of the sublist
# etc.
# [5, 1, 10, 50, 25, 12]
# [5, 1, 10, 12, 25, 50]
# [5, 1, 10, 12, 25, 50]
# [5, 1, 10, 12, 25, 50]
# [5, 1, 10, 12, 25, 50]
# [1, 5, 10, 12, 25, 50]

def max_i(L1):
    cur_max = L1[0]
    cur_max_i = 0
    for i in range(1, len(L1)):
        if L1[i] > cur_max:
            cur_max = L1[i]
            cur_max_i = i
    return cur_max_i
# complexity analysis:
# same amount of time every time
# repeats len(L1)-1 times
# runtime: O(L1)
# k1*len(L1)

def selection_sort(L):
    # n = len(L
    for j in range(len(L)-1): # everything except line 35: k3*n
        ind_of_max = max_i(L[:(len(L)-j)]) # (k1+k2)*(n-j)
        # k1 is max_i(L)
        # k2 - creating list of n-j
        ind_of_end = len(L) - j - 1
        L[ind_of_max], L[ind_of_end] = L[ind_of_end], L[ind_of_max]

# complexity analysis:
# if j is very large, then need to find the max of a large list, takes longer than if j is small
# slicing - creates a new list
# the longer the list needed to copy, the longer the time

# all of the iterations on 35: (k1+k2)*(n+(n-1)+(n-2)+..+1) = (k1+k2)*n*(n+1)/2
# 1+2+3+....+n = n(n+1)/2
# TOTAL: k3*n+(k1+k2)*n*(n+1)/2
    #  = 0.5(k1+k2)n^2 + (k3(k1+k2)/2)n + 0.5(k1+k2) ... care about the highest order term, so this is O(n^2)

def max_i_full(L, right_end):
    cur_max = L1[0]
    cur_max_i = 0
    for i in range(1, len(L1)):
        if L1[i] > cur_max:
            cur_max = L1[i]
            cur_max_i = i
    return cur_max_i

    # Runtime of max_i: O(right_end)
    # In seconds: k1*len(L1)

def selection_sort(L):
    # n = len(L
    for j in range(len(L)-1): # everything except line 35: k3*n
        ind_of_max = max_i_full(L, len(L)-j) # (k1)*(n-j)
        # not copying the entire L, so it's faster
        ind_of_end = len(L) - j - 1
        L[ind_of_max], L[ind_of_end] = L[ind_of_end], L[ind_of_max]
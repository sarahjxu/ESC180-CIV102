# John von Neumann's MergeSort
# CPython uses TimSort, which is a variant of MergeSort

# 1. sort of first half of the list
# 2. sort of second half of the list
# 3. merge the results of 1 and 2

[5, 4, 1, 10, 2, 3, 1, 4]

[5, 4, 1, 10]  [2, 3, 1, 4]

[5, 4]  [1, 10]  [2, 3]  [1, 4]

[5]  [4]  [1]  [10]  [2]  [3]  [1]  [4]

[4, 5]  [1, 10]  [2, 3]  [1, 4]

[4, 5, 1, 10]  [2, 3, 1, 4]

[1, 4, 5, 10]  [1, 2, 3, 4]

[1, 1, 2, 3, 4, 5, 10]


1 1 ....... 1 1 k3*m
n/4 n/4 n/4 n/4 k3*m
n/2 n/2         k3*m
n               k3*m
total runtime(log2n + 1)k3n
+1 since that many levels (0 to n levels so +1)
O(nlogn)


def merge_slow(L1, L2):
    return sorted(L1+L2)

def merge(L1, L2):
    '''return a list sorted(L1+L2), assume L1 and L2 are sorted in non-decreasing order'''

    i, j = 0, 0 # currently looking at L1[i], L2[j]
    merged = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    merged.extend(lis1[i:])
    merged.extend(lis2[j:])
    # in total appends len(L1)+len(L2) elements to merge
    # each append operation takes the same amount of time
    # so the runtime is k*en(L) (L = L1+L2)

    return merged

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    mid = len(L) // 2
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))
    # intotal, each call takes k3*n
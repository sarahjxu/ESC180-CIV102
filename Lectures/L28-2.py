# [1, 5, 2, 1, 6, 2, 5]

# counts
# 0 1 2 3 4 5 6
# 0 2 2 0 0 2 1  --> the number of each element
# [1, 1, 2, 2, 5, 5, 6]

# counting sort

def counting_sort(L):
    counts = [0]*(max(L)+1) #k1*len(L) [for finding max] + k2*max(L) [for creating the list]
    for e in L: # k3*len(L)
        counts[e]+=1

    sorted_L = []
    for i in range(len(counts)): #k5*max(L) since line 16 is k4*len(L)
        sorted_L.extend([i]*counts[i]) # k4*counts[i] time

    # total for line 17: k4*(counts[0]+counts[1]+...+counts[max(L)]) = k4*len(L)

    L[:] = sorted_L # L = sorted_l #k6*len(L)

# TOTAL: c1*len(L) + c2*max(L)
# c1 = k1+k3+k4+k6
# c2 = k2+k5

# if len(L) > max(L) then c1*len(L) + c2*max(L) < (c1+2)*len(L)
# O(len(L)+max(L)) or O(max(len(L), max(L))
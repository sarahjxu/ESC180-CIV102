# Aliasing

L1 = [5, 6, 7]
L2 = L1 # any time you change contents of L1, it's the same as changing L2; changing L1[0] changes L2[0] as well

L2 = 5 # L1 is unchanged. Take address where 5 is, write in variable table that L2 now refers to address where 5 is
# if LHS there is element of list, modify memory table, if LHS is variable, etc, then modify variable table

################## addressing issues in aliasing

# Shallow copy

L1 = [5, 6, 7]
L2 = L1[:] # shorthand for L2 = [L1[0], L1[1], L1[2]]

L1[0] = 99 # L2[0] is unaffected --> L1 and L2 are separate lists now

# shallow copy creates issues for lists of lists

L1 = [[1, 2], [3, 4]]
L2 = L1[:] # so we copied each list into L2; L1 and L2 are separate lists but the elements of each inner list is the same
# so changing inner list will change L2, changing list won't affect L2

L1[0] = 99 #l2[0] is unaffected
L1[1][0] = 00 # L2[1][0] is also

# Deep copy
# A list that's completely independent of L1

L1 = [[1, 2], [3, 4]]
L2 = [[L1[0][0], L1[0][1]], [L1[1][0], L1[1][1]]]

id(L1[0][0]) == id(L2[0][0]) # but this doesn't matter, as we can't change the contents of integers
# so changing L1[0][0] assigns a different value there, but does not change the value of 1, so L2[0][0] stays the same

L1 = [[1, 2], [3, 4]]
L2 = []

for sublist in L1:
    L2.append(sublist[:])
    # when python sees sublist[:], it creates a new list with the same contents as sublist but separate from sublist

L1 = [[[1]]] # a list of lists of lists of integers
L2 = []

for sublist in L1:
    L2.append(sublist[:])

    # creates a shallow copy of [[1]]

L2[0][0][0] = 99

L1 = [[[1]]]
L2 = []
for sublist in L1:
    sublist_copy = []
    for subsublist in sublist:
        sublist_copy.append(subsublist[:])
    L2.append(sublist_copy)

L1 = [[1, 2], 5]
# causes problems...can't do the same approach since 5 is not a list
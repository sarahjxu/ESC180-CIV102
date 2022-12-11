L1 = [[1, 2], [3, 4]]
L2 = L1[:]
# L1[0][0] = 5
# L2 also has L2[0][0] = 5
# ... avoid that?

copy = []
for e in L1:
    copy.append(e[:])
    # copy.append(e) --> JUST REFERRING DIRECTLY TO [1, 2], SO ANY CHANGES STILL OCCUR ON COPY


L1 = [[1, 2], [3, [4, 5]]]
# if you change L1[1][1][0], then it changes in L2 as well, as the list [4, 5] was a shallow copy, the rest are deep copies

def deep_copy(obj):
    '''Return a deep copy of the list of lists of ..... lists of integers obj'''


    # base case
    if type(obj) != list:
        return obj

    # recursive step: obj is a list
    copy  = []
    for elem in obj:
        copy.append(deep_copy(elem))
    return copy

copy = deep_copy(L1)

impot copy
copy.deepcopy([1, 2, 3]) # does the same thing
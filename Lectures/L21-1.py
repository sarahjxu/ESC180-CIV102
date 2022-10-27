# Sparse matrices
# [5 0 0]
# [2 0 1]
# very wasteful for memory

# [5 _ _]
# [2 _ 1]

dim = 2, 3
M1 = [[0] * dim[1]] * dim[0]
M1[0][0] = 5 # changes both rows, aliases
# the 0 in dim[1] is also alias, but doesn't matter

def sparse_M_v(M, v, dim):
    res = [0] * dim[0]
    for coords, entry in M.items():
        res[coords[0]] += entry * v[coords[1]]
    return res

M = {(0, 0): 5, (1, 2): 1, (1, 0): 2}

sparse_M_v(M, [1, 2, 3], (2, 3))
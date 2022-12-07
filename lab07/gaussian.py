import numpy as np

def print_matrix(M_lol):
    M = np.array(M_lol)
    return M

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

def get_row_to_swap(M, start_i):
    smallest_ind = len(M)
    smallest_row_ind = start_i
    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) <= get_lead_ind(M[start_i]):
            if smallest_ind != get_lead_ind(M[i]):
                smallest_ind = min(smallest_ind, get_lead_ind(M[i]))
                if smallest_ind == get_lead_ind(M[i]):
                    smallest_row_ind = i
    return smallest_row_ind

def add_rows_coefs(r1, c1, r2, c2):
    new_list = [0]*len(r1)
    c1r1 = np.dot(r1, c1)
    c2r2 = np.dot(r2, c2)
    for i in range(len(new_list)):
        new_list[i] = c1r1[i] + c2r2[i]
    return new_list

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub+1, len(M)):
        c1 = -M[i][best_lead_ind]/M[row_to_sub][best_lead_ind]
        M[i] = add_rows_coefs(M[row_to_sub], c1, M[i], 1)
    return M

def forward_step(M):
    for i in range(len(M)):
        M[get_row_to_swap(M, i)], M[i] = M[i], M[get_row_to_swap(M, i)]
        eliminate(M, i, get_lead_ind(M[i]))
    return M

def backward_step(M):
    for i in range(len(M)-1, -1, -1):
        best_lead_ind = get_lead_ind(M[i])
        for j in range(i-1, -1, -1):
            c1 = -M[j][best_lead_ind]/M[i][best_lead_ind]
            M[j] = add_rows_coefs(M[i], c1, M[j], 1)
    for i in range(len(M)):
        c = get_lead_ind(M[i])
        M[i] = np.dot(M[i], 1/M[i][c])
    return M

def solve_mxb(M, b):
    for i in range(len(M)):
        M[i].append(b[i])
    forward_step(M)
    backward_step(M)
    x = []
    for i in range(len(M)):
        x.append(M[i][len(M[0])-1])
    return x

### Using NumPy

# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
#print(M)




#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)

#print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist()

#print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

### Testing cases
# 1
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# print(print_matrix(M_listoflists))

# 2
# row1 = [1, -2, 3]
# row2 = [0, 0, 0]
# row3 = [0, 1, 1]

# print(get_lead_ind(row1))
# print(get_lead_ind(row2))
# print(get_lead_ind(row3))

# 3
# M = [[5, 6, 7, 8],[0, 0, 0, 1],[0, 0, 5, 2],[0, 1, 0, 0]]
# M1 = [[5, 6, 7, 8],[0, 0, 1, 1],[0, 0, 5, 2],[0, 0, 0, 1]]
# print(get_row_to_swap(M, 1))
# print(get_row_to_swap(M1, 1))

# 4
# print(add_rows_coefs([2, 3, 4], 5, [1, 3, 4], 5))
# print(add_rows_coefs([2, 3, 4], 5, [2, 3, 4], 5))

# 5
# M = [[5, 6, 7, 8],
# [0,0, 1, 1],
# [0, 0, 5, 2],
# [0, 0, 7, 0]]
# row_to_sub = 1
# best_lead_ind = 2
# print(eliminate(M, row_to_sub, best_lead_ind))

# 6
# M = [[ 0, 0, 1, 0, 2],
# [ 1, 0, 2, 3, 4],
# [ 3, 0, 4, 2, 1],
# [ 1, 0, 1, 1, 2]]
# forward_step(M)

# 7
# M = [[ 1, -2, 3, 22 ],
# [ 0, 16, -8, 248],
# [ 0, 0, 3.5, -38.5]]
# print(backward_step(M))

# 8
# M = [[ 0, 0, 1],
# [ 1, 0, 2],
# [ 3, 1, 4]]
# b = [1, 2, 3]
# print(solve_mxb(M, b))
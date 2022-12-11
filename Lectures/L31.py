# recursion

L = [12, 10, 2, 10, 2]

def sum_list(L):
    '''Return the sum of the list of integers L
    Define the sum of the empty list to be 0'''

    if len(L) == 0: # base case
        return 0
    return L[0]+sum_list(L[1:])

# sum_list([])
# return 0

# sum_list([2])
# return 2 + sum of []

# sum_list([10, 2])
# return 10 + sum of 2...

# sum_list([2, 10, 2])
# return 2 + sum of 10...

# sum_list([10, 2, 10, 2])
# return 10 + sum of 2...

# sum_list([12, 10, 2, 10, 2])
# return 12+sum of 10...

# complexity:
# excluding the call to the list, takes the same amount of time --> just checking foor L[0]
# we call sum_list len(L) + 1 times
# each call (excluding calls to sum_list) takes the same amount of time
# Runtime complexity: O(len(L))  (O(n) where n = len(L))
# how long does splicing take? here we assume that splicing takes constant amount of time (...incorrect assumption)
# splicing isn't part of the algorithm

def sum_list2(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]

    mid = len(L)//2 # divided using integer division to get whole numbers for indexing

    return sum_list2(L[:mid]) + sum_list2(L[mid:])
    # up to the middle, not including the middle and starting from the middle

# sum_list([2])
# return 2 + sum of []

# sum_list([10, 2])
# return 10 + sum of 2...

# sum_list([2, 10, 2])
# return 2 + sum of 10...

# sum_list([10, 2, 10, 2])
# return 10 + sum of 2...

# sum_list([12])  sum_list([10])   sum_list([2])  sum_list([10])    ...   sum_list([2, 1]) sum_list([2, 3, 4])
# sum_list([12, 10])     sum_list([2, 10])         sum_list([2, 1]) sum_list([2, 3, 4])
# sum_list([12, 10, 2, 10])           sum_list([2, 1, 2, 3, 4])
# sum_list([12, 10, 2, 10, 2, 1, 2, 3, 4])

# the complexity of sum_list2 is the same as sum_list 1
# the tree branches out and basically works from left to right (does one "diagonal" at a time)
# depth: log_2(n) --> 1 + 2 + 3 + ... + 2^(log2(n))
# geometric series
# 1+2+4+...+2^k = (2^(k+1)-1)/(2-1)
# what is k? log2n

# each call to sum list takes the same amount of time (approximation due to splicing, if the list is larger, the splicing will probably take more time)

def f(L):
    mid = len(L)//2
    f(L[:mid])

def g(L, start, end):
    mid = (start+end)//2
    g(L, 0, end)

# f(L) and g(L) are the same, but f(L) takes longer if list is longer
# for g(L), itt akes hte smae amount of time no matter what mid is, always passing the same list L

def sum_list2(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]

    mid = len(L)//2

    return sum_list2(L[:mid]) + sum_list2(L[mid:])

# when you get to summing a list of 1 elemenet, would cause infinite recursion since its 1 element + 0 forever, so you stop it by specifying that if length is 1, just return L[0]

# n = len(L)
# how many calls to sum_list2 are there in total?
# 1, 2, 4, 8....


# [1] [1] [1] [1] ... [1] [1] [1] [1]     ...n calls
#    .....
#        [n/4] [n/4] [n/4] [n/4]          ...4 calls
#            [n/2]   [n/2]                ...2 calls
#                 [n]                     ...1 call


# sum of the geometric series: 1 + r^1 + r^2 + ... + r^k = (1-r^(k+1))/(1-r)
# total calls? 1 + 2 + 4 +...+ n
# 1 + 2^1 + 2^2 + 2^3 + ... + n
# 1 + 2 + 3 + ... + 2^(log2n) = (1-2^(log2n+1))/(1-2) = 2*2^log2n - 1 = 2n-1
# 2^log2n --> how many levels are there, also since we are going with 2 as the base for geometric, so 2^log2n = n

#...and at the end, it is still O(n) complexity, n = len(L)

# why does this happen as O(n)?
# the tree is very wide and very shallow
# as many calls in last line as all other lines
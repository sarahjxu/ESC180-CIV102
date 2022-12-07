# factorial
# n calls n-1 calls n-2...levels to go from n to 1?
# each call takes the same amount of time
# O(n)

# power
# n calls n/2 calls n/4....levels to go from n to 1?
# log2n --> O(logn)

# 2^n slow
# n calls n-1 (2) calls n-2 (4) calls n-4 (8)
# 1+2+4+8+.... amount of calls (add up the number of calls on each level)
# O(2^n)

# sum list
# merge sort-like version
# n calls n/2 (2) calls n/4 (4) calls n/8 (8)
# 1+2+4+8+...+2^(log2n) --> 1 call per element of the list
# == 2n-1
# complexity? code takes different amount of time --> length is O(n) if sum up all the instances on one level, and number of levels? logn?
# O(nlogn)

# sum list fast
# no slicing, use mid
# each call takes the same amount of time, not creating copies of lists with slicing
# O(n)

# mergesort
# n calls n/2 (2) calls (n/4)....2n-1 calls
# complexity: merge operation takes time proportional to total size of list
# on each level after adding all calls, it takes time proportional to n...sum all levels
# O(nlogn)
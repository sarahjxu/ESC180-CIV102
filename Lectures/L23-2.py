# efficiency of algorithms

L = [1, 2, 5, 0, 9]
e = 10
L.find(e)

def find_i(L, e):
    # 2 operations to initialize
    for i in range(len(L)): # 2 operations (increment counter, put in i)
        if L[i] == e: # 3 ops )L[i], L[i] == e, if)
            return i # 1 op
    return -1 # 1 op
    # 3+ 5 *n ops in the worst case

# worst case runtime complexity for an input of size n
# count the number of operations needed to complete the run of the function, in the worst case (when you don't return early)
# the upper bound on the worst case runtime: t*(3+5*n)
# runtime approximately proportinal to n
# 3*t + 5*t*n (first term doesn't matter, too small)
# the upper bound on the worst case runtime complexity of find_i is O(n)

# F is O(g) if lim sup (n--> infinity) f(n)/g(n) < infinity
# sup = least upper bound
# want g(n) to grow at least as fast of f(n)
# then f(n) is O(g)

# eg. f(n) = n, g(n) = 0.001n^2
# eventually g(n) will overcome f(n)
# f(n)/g(n) eventually will go to 0
# if h(n) = 0.0001n, f and h grow at same rate, f is O(h), h is O(f)

# why have sup? in the case that f and g are oscillating
# there is no upper as they oscillate, but in the example, f and g are growing at the same rate
# sup:
# lim               [lub    {f(n)/g(n)}]
# (n --> infinity)   N > n

# 2n^2 + n is O(n^2)
# lim n--> infinity (2n^2 + n)/n^2 = 2
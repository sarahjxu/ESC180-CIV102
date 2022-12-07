def find_i(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return i
    return -1

# A simple expression for a tight upper bound on the worst-case runtime complexity, using big O notation
# O(n) for n = len(L)
# O(len(L))

# How fast is find_i?
# In general, it'll run in time proportinal to len(L)

# the runtime is proportional to t*(5 + 3n)

# technically true;
# (5 + 3n) is O(n)     # tight upper bound
# (5 + 3n) is O(n^2)   # not tight upper bound
# (5 + 3n) is O(0.000001n + log(n))   # tight upper bound, not the simplest form
# constants don't matter, lower order terms don't matter (any terms in a sum that don't grow as fast as the fastest term)
# we want a TIGHT upper bound, choose O(n) not O(n^2)

# 0.000001n + log(n) < 2n, is O(n)


# procedure
# 1. count the elementary operations
# 2. come up with a forumla for the number of operations in terms of the size of the input, for the worst case
# 3. simplify the expression

# if a loop runs k times, and each iteration takes the same amount of time, then the loop runs in O(k) time
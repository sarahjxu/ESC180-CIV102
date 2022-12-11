# 1, 1, 2, 3, 5, 8, 13...

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)



# fib(n)








# 1
# ...                              1
#   ...                        ...           ... } n levels, all full
#      (n-4) (n-3)  (n-3) (n-2)                4
#         (n-2)        (n-1)                   2
#                 n                            1
# but the branch on the right is longer than the branch on the left
# so lets pretend the problem doesn't exist and there are n levels in total
# We have fewer than 1 + 2 + 3 + 8 + ... 2^n = (2^(n+1)-1)/(2-1) = 2^(n-1)-1
# We have O(2^(n+1)) = O(2^n) calls (upper bound)


# the left is n/2 elvels

# we have more than 1 + 2 + 4 + ... + 2^(n/2) = (2^(n/2)+1)-1)/(2-1) = 2*sqrt(2)^n
# We have O(sqqrt(2)^n) as a lower bound

# but when talking about complexity, say upper bound --> so only say O(2^n)

# but we can do better!

# Define T(n) as the runtime of fib(n)
# T(n) = const + T(n-1) + T(n-2) ==> const = check for n <= 2
# if const very small, T(n) works like fib(n)
# T(n) ~ a*fib(n)
# We can say that the worst-case runtime complexity of fib(n) is O(fib(n)) ... an approximation

# 1 + a + a^2 + .. + a^q = (a^(q+1)-1)/(a-1)

import math

def fib_formula(n):
    phi = (1+math.sqrt(5))/2
    return int((phi**n/math.sqrt(5)) + 0.5)

# so fib_formula(n) and fib(n) return the same number


# sqrt(2) = 1.41 # lower bound is 1.41^n
# phi = 1.61
# 2 = 2 # upper bound is 2^n
# we can approximate the golden ratio!



# not efficient..if we compute fib(n-2) once, don't want to do it again!
# Caching
# Storing values that the recursive function computes

# cashe = {1:1, 2:1, 3:2, 4:3, 5:5...}

def fib_cache(n, cache):
    if n in cache:
        return cache[n]
    cache[n] = fib_cache(n-1, cache)+fib_cache(n-2, cache)
    return cache[n]

cache = {1:1, 2:1}
fib_cache(20, cache)


def fib_iter(n):
    fib_prev = 1
    fib_cur = 1
    if n<=2:
        return 1
    for i in range (3, n+1):
        # fib_cur = fib(i)
        # fib_prev = fib(i-1)
        fib_prev, fib_cur = fib_cur,fib_prev + fib_cur
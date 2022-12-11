def power(x, n):
    '''return x^n'''
    res = 1
    for i in range(n):
        res *= x
    return res

# O(n)

def power_rec(x, n):
    '''Return x^n'''
    if n == 0:
        return 1
    return x*power_rec(x, n-1)
    # calls go from n to 0
    # n + 1 calls so complexity is O(n)

# do better?
# x^n = x*x^(n-1)
# x^n = x^(n/2)^2
    # this is better, if you half n every time, it is a lot fewer steps

def power_rec2(x, n):
    '''Return x^n
    n -- an integer
    x -- a non-zero real number'''

    if n == 0:
        return 1
    if n == 1:
        return x # x = x^1

    half_power = power_rec2(x, n//2)

    # x^n = half_power*half_power (*x if n is odd)

    if n % 2 == 0:
        return half_power*half_power
    else:
        return half_power*half_power*x




# 1
# ...
# n/4
# |
# n/2
# |
# n


# from the top: 1, 2, 4, 8 ... n
# how many steps?
# log2(n), so that is why this is the complexity:
# O(log2(n)) (same as O(logn))


# 2^0, 2^1, ..., n
# .............. 2^k
# 2^k = n
# k = log2n
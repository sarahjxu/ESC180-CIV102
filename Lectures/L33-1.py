def fact_while(n):
    cur_prod = 1  # cur_prot = (i-1)!
    i = 1

    while i != n+1:
        cur_prod *= i
        i += 1
        # invariant: cur_prod = (i-1)!

    # i = n+1
    # cur_prod = (i-1)! = (n+1-1)! = n!

    return cur_prod

def f(a = 2, b = 3):
    return a + b

# f(10) = 10 + 3 = 13
# f() = 2 + 3 = 5
# default values for a and b, if no argument is given for a, b, or a and b, then the sum of initial value(s) happens


def fact_iter(n, cur_prod = 1, i = 1):
    '''return n! Arguments:
    n -- an integer
    cur_prod = (i-1)!
    '''
    if i == n+1:
        return cur_prod

    return fact_iter(n, cur_prod*i, i+1)

# this is the same as fact_while
# with cur_prod and i as defaults, we can do things like: fact_iter(5)

# fact_iter(3, 1*2*3, 4 \
# |                     6
# fact_iter(3, 1*2, 3)/
# |                   \
# fact_iter(3, 1*1, 2)   \6
# |                  /
# fact_iter(3, 1, 1) \
#                     6
# computing upstream

def fact_rec(n):
    if n == 0:
        return 1
    return n*fact_rec(n-1)

# computing downstream
# fact_rec(0) \
#              1
# fact_rec(1)/
#            \ 1*1
# fact_rec(2) /
#             \ 1*1*2
# fact_rec(3)  /
#              \ 1*1*2*3

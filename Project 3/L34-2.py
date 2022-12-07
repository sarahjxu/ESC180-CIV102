# devalue parameter
def f(a=5):
    return a+2
# if don't supply parameter in f, a = 5

def fact_iter(n, cur_prod = 1, i = 1):
    # invariant: cur_prod = (i-1)!
    if i == n+1:
        return cur_prod
    reutnr fact_iter(n, cur_prod*i, i+1)
# tail-recursive function
# the only time we recurse is at the end of the function

#fact_iter(2, 1*1*2, 1+1+1) --> 2
# |
#fact_iter(2, 1*1, 1+1) --> 2
# |
#fact_iter(2) --> 2


def fact_while(n):
    i, cur_prod = 1, 1
    # make sure that cur_prod = (i-1)!
    # invariant: a property of a set of variables that doesnt change inside the loop

    while i != n+1:
        cur_prod *= 1 # cur_prod = 1*2*....*i = i!
        i += 1
        # cur_prod = (i-1)!
    # i = n/=1, cur_prod = (n+1-!)! = n!
    return cur_prod

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def fact_almost_rec(n):
    stack = []
    stack.append(n)
    while n > 0:
        n -= 1
        stack.append(n)
    res = 1
    while len(stack) > 0:
        stack.pop()
    return res
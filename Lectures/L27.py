def f(L):
    for i in range(len(L)):
        pass

# complexity of f: O(n),n = len(L)
# runtime: ~ 0.00000001 + 0.00002*len(L) seconds --> but depends on the computer itself

def g(L):
    for i in range(int(len(L)**(1.3))):
        pass

# complexity of g: O(n^0.3333333)

def h(L):
    #0.5n
    for i in range(len(L)//2):
        # 10000n
        for j in range(len(L)*10000):
            pass

# runs 5000n^2 times
# runtime proportional to n^2, n = len(L)
# the 5000 is irrelevant, since each iteration takes some amount of seconds, multiply by 10000, is another constant
# eg. each iteration takes t1 seconds, so total runtime is 5000*t1*n^2, so 5000*t1 is a constant, wo don't know t1
# O(n^2), where n = len(L)

def log10(n):
    res = 0
    while n > 1:
        n /= 10
        res += 1
    return res

# n, n/10, n/100...
# runtime complexity: O(log10(n)) = O(log(n))


# k is the number of steps to go from n to 1
# n = 10^k => log10(n) = k = log10(10^k)
# ...
# 100 = 10^2
# 10 = 10^1
# 1 = 10^0

def square(n):
    res = 0
    for i in range(n):
        res += n
        # assume += takes the same amount of time each time, so need floats
    return res

# O(n)

### examples of infinite loops
'''
def f():
    while True
    pass
'''

'''
def g():
    n = 3
    while True:
        if n % 2 == 0 and is_prime(n):
            return
        n += 1
'''

'''
def fermat(p):
    n = 1
    while True:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    if i**p+j**p == k**p:
                        return i, j, k
'''

def f(n):
    return n+2

import inspect
source = inspect.getsource(f)
print(source)

def halt(f, x):
    '''return True if f halts (ie, doesn't loop infinitely) if given input x'''

def confused(f):
    if halt(f, f): # if f halts on its own source code, then do an infinite alt
        while True:
            pass
    else:
        return False
    # if it's possible to write halt it's possible to write confused

confused(confused) # consider plugging confused into itself

# Assume confused(confused) is not False
# it must be that we are in the infinite loop (there is an infinite loop in confused(confused)
# but the only way to get an infinite loop is when confused halts on confused
# halt(confused, confused) is True
# which means that there is no intinite loop confused(confused)

# assume confused(confused is not False
# => there is an infinite loop inside confused(confused)
# => halt(confused, confused) is True
# there is no infinite loop confused(confused)

# assume confused(confused) is False
# => there is no infinite loop in confused(confused)
# => halt(confused, confused) is True
# => there is an infinite loop in confused(confused)

# the assumption is wrong! Assumption: halt is possible to write

# Halting Problem (due to Alan Turing)

# Goedel's Incompleteness Theorem:
# There are true statements about math that are not provable

# Assume that any statement is provable false or true
# => make an algorithm for halt()
# => but halt doesn't exist
# => the assumption that any statement is provably true or false is false

def halt(f, x):
    # try all English statements of length 1, 2, 3....
    # if s is a proof that f halts on input x, return True
    # if s is a proof that f does not halt on x, return False
    # eg. cannot prove or disprove there is a set that is smaller than natural numbers, larger than real numbers
# Recusion
# functions calling themselves as helper functions

# fib(n) = round(phi^n/sqrt(5)), phi = (1+sqrt(2))/2

# fibonacci numbers: 1, 1, 2, 3, 5, 8, 13 ...
# fib(n) = fib(n-1)+fib(n-2)+...
# fib(1) = fib(2) = 1

def fib(n):
    if n<= 2: # base case
        return 1
    else:
        return fib(n-1)+fib(n-2)

def minus1(n):
    if n == -15:
        return 0
    print(n)
    return minus1(n-1)

# minus1(-15) --> 0
# minus1(-14) --> 1
# minus1(-13) --> 2
# ...
# |
# minus1(4)
# minus1(5) # the return value the total number of


# 1. to find the answer you must know the answer
# 2. you can't push on a rope: must have a base case
# 3. F = ma

def is_even(n):
    '''return True fiff n is an even number, assume n >= 0'''

    # if not is_even(n-1):
    #     return True
    # else:
    #     return False
    if n == 0:
        return True
    return not is_even(n-1)

    # O(n)

def is_even_for(n):
    is_even_cur = True # is i even?
    for i in range(n):
        is_even_cur = not is_even_cur
    return is_even_cur

def is_even_while(n):
    i = 0
    is_even_cur = True # is i even?
    while i <= n:
        i += 1
        is_i_even - not is_i_even
    return is_i_even

def print_list_forward(L):
    '''Print out the list L element by element'''
    if len(L) == 0:
        return
    print(L[0])
    print_list_forward(L[1:]) # k*(n-1) time
    # does not take the same amount of time, splicing doesn't take the same amount of time each time
    # O(n^2) --> k(n-1 + n-2 + ... + 1)

# print_list_forward([7]) 7
# print_list_forward([6, 7]) 6
# print_list_forward([5, 6, 7]) 5

def print_list_backward(L):
    if len(L) == 0:
        return
    print_list_backward(L[1:])
    print(L[0])
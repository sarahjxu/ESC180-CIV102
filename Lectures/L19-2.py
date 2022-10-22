# tuples
# like lists, but immutable

t = (1, 2, 3, 4)
t[0]
# t[0] = 5 makes error

t1 = ([1, 2], 3)
t1[0][0] = 99 # this is ok, since the element of the tuple is mutable

t = 2, 3, 4 # can leave out the parentheses
a, b, c = t # a = 2, b = 3, c = 4
# this is called unpacking tuples
# need the same number of elements: a, b = t creates error
a, b = b, a
# for variable swapping --> also creating tuples

# tuples are useful for returning multiple values

def f():
    return 42, 43 # (42, 43)

t_res = f()
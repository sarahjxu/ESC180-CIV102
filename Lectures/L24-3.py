import timeit

s = '''def f():
    res = 0.0
    for i in range(1000000):
        res += i

f()'''

def f():
    res = 0.0
    for i in range(1000000):
        res += i

def g():
    for i in range(1000):
        print(i)

# g()

print(timeit.timeit(s, number = 10))
# print(timeit/timeit("f()", number = 10)) # gives error
# f() is not defined inside the quotes when calling timeit
print(timeit.timeit("f()", number = 10, globals = globals()))
#globals() --> calling the globals dictionary
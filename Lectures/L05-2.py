# communicating to a function:
# 1. pass an argument
# 2. have the function access a global variable
# usual way to communicate to function is to pass to an argument

def f(x):

def g():
    # if you say y = 5, then it overshadows the global y = 6
    return y**2

# communication from a function
# 1. return a value
# 2. set a global variable to the result

def h(x):
    return x**2

def i(x):
    global res
    res = x**2
    # THIS IS NOT THE USUAL THING TO DO. DO #1 UNLESS GOOD REASON TO DO #2

if __name__ == '__main__':
    a = f(5)
    # take 5 and pass it to x. x becomes 5
    y = 6
    b = g()
    # g() accesses y. y is a global variable, so you don't have to say global y
    # when accessing values, don't need to define global/local. if changing values, need to specify if you want it to carry over to other places
    i(20)
    print(res)
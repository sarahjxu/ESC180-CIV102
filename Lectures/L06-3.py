# control flow with return

# return
def f(x):
    print("I'm about to compute a square, hooray!'")
    return x**2
    print("hi") # doesn't execute
# once you hit return, it's the end of the function. lines after the return don't happen

# functions in python go line by line

def artsie_math(arg1, arg2, op):
    '''Return arg1 <op> arg2 for op "+" and "-", otherwise print "It's too complicated for me"'''
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    else:
        print("It's too complicated for me")

def artsie_math1(arg1, arg2, op):
    if op != "+" and op != "-":
        print("It's too complicated for me")
        return # None --> this return statement might be a problem later if we use the result
        # called an early return
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
# two different if statements here
# first check if its neither +  or -. If it is true, then return, never get to if + and elif -
# when defining 2 functions one after the other, with the same name, the later one overwrites the original (even when parameters change)

if __name__ == "__main__":
    print(f(5))
    artsie_math(5, 6, "+") # 11
    res = artsie_math1(5, 6, "*") # print "too complicated..."
    print(res) # the issue with line 24!
    # print(res + 5) GETS AN ERROR FOR RETURN NONE. WHEN WE RETURN THE NUMBERS, IT STILL WORKS
    # want to avoid this

    if res != None:
        print(res + 5)
    else:
        print("The artsie messed up earlier")
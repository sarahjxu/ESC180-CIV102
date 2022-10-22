# globals: my_res = 25
# f(y) = y^2

def f(x):
    res = x**2
    return res

if __name__ == '__main__':
    # my_res = f(5)
    # print(my_res)
    # print(x) and print(res) both don't work...they are both not global variables

    print(my_res)
    my_res = f(6)
    print(my_res)

    # these 3 lines give you 25, 26 as results
    # somehow saves the previous input of f(5) when I rant it earlier
    # if you clear the environment and restart (press the x)
    # then when you run it, there will be error --> my_res is not defined
    # this is specific to pyzo
def my_sqrt(x):
    sqr = x**.5
    return sqr

def my_print_square(x):
    sqr = x**.5
    print(sqr)

if __name__ == "__main__":
    res = my_sqrt(25)

# run up to this point returns nothing --> have not asked the program to do anything yet

# print(sqr)

# executing this produces error, we are asking python to print sqr, a variable which is not defined globally. There is an sqr defined locally inside the function my_sqr, but it loses value outside of the function

    res = my_print_square(25)
    print(res)

    # print(res) returns None, as the result of the previous function is printing a value, such that the function has no value anymore...so printing the function with no value results in None
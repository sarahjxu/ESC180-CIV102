def test_for():
    for _lq98uwqeqweiwqi in range(5):
        print(_lq98uwqeqweiwqi)

    for i in range(1, 5):
        print(i)

    for i in range(1, 7, 2):
        print(i)
        # start at 1, to 7 but not including 7, in steps of 2

    for i in range(1, 6, 2):
        print(i)
        # from 1, to 6, but not including 6, in steps of 2

    for i in range(9, 2, -2):
        print(i)
        # from 9, to 2, but not including 2, in steps of 2

    for i in range(1, 9, -1):
        print(i)

def print_while_pos(start, end, step):
    '''print all the integers in the range start...end with a step step'''
    i = start
    while i < end:
        print(i)
        i += step # i = i + step
    # usually use for loops instead of while, need the while condition to be correct for no infinite loop

def print_while(start, end, step):
    i = start
    if step > 0:
        while i < end: # sign(i-end) is positive
                       # sign(i-end)*sign(step) is positive
            print(i)
            i += step
    elif step < 0:     # sign(i-end) is positive
                       # sign(i-end)*sign(step) is negative
        while i > end:
            print(i)
            i += step
    # IN GENERAL, REPEATED CODE SHOULD BE AVOIDED

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def print_while2(start, end, step):
    i = start
    while sign(i-end)*sign(step) < 0:
        print(i)
        i += step


if __name__ == '__main__':
    print_while(5, 1, -2)
# how to test code to make sure it works properly
# test all typical cases
# test edge cases and boundary cases
    # on the boundary between inputs that are allowed and not allowed

# error cases:
    # eg. dividing by 0 - calculator should print error, instead of code crashing
    # eg. string and float - calculator should print error, instead of code crashing
    # eg. having a very large number (int), then multiplying by another large number (int), or adding any number ... the
        # code won't crash. BUT if you have a very large number (float), then multiplying by another large number/adding
        # very large number will cause the code to crash
    # for errors: should you be able to undo/store/perform operations on an ERROR?

# if you have a file called test_calc, then you can import test_calc into another file

# eg.

import test_calc

# BUT, things inside the "__main__" block of test_calc will not run from the import
# if you say print("hi") outside the main block, it will run if you call import test_calc
# all the functions defined outside the main block will all be fair game
# calling any functions from test_calc in another file --> need to use test_calc.add, for example
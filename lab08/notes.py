# Problem 1

# Debugging infinite loop by interrupting the rpogram and using postmortem debugging

# 1. ctrl+i to interrupt
# 2. shell --> postmortem
    # takes you to the location where the issue occurred
    # we see that there is an infinite loop since move_y is always greater than 0
    # comment out the while loop and use a for loop instead
    #  ctrl-i to exit the debugging

# Identifying a failing test case, extracting the input that would cause the test case to fail, and then tracing through the function that returns the incorrect value

#1. run tester.py
#2. it shows that the test for search_max failed, so we set up a breakpoint at the search_max call, line 13 and step through to see what is going on
    # shows you that search_max is wrong, since we are returning a random number
    # fix this -- for this case, we can just return the expected value, but it won't work for other cases - need to use for loop to fix
#3. so let's see what is wrong with detect_row
    # we print the board out from stepping into test_detect_row and the two test functions
    # we look at detect_row_bad and it shows that it wants to print only for (5, 1, 0, 1, 3) parameters, but the input parameters start with 0 -- this will not return (1, 0), thus failed.
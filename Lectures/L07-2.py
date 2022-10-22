# repeated computation ("loops")

# set i to 0, then 1, then 2, ... then 4
# and repeat the block of code inside

# for loop

def for1():
    for i in range(5):
        print(i)
        print(2*i)
        print("=============")
    # loop indices always start from 0!
    # start at 0, go up to and not including 5
    # repeat 5 times

def for2():
    for i in range(1000):
        print("I'm telling you for the " + str(i) + "-time, EngSci rocks")

# compute a^b
# 1 * a * a * a * a * a... b times
def my_pow(a, b):
    '''return a^b for a non-negative integer b'''
    res = 1
    for i in range(b):
        res = res * a
    return res

# when you don't know how long you want to repeat a piece of code...while loop
# while <condition>:
    # <block>
# repeat the block while the condition is true

def while1():
    i = 0
    while i < 5:
        print(i)
        i = i + 1
# difference between while and if?
# while - goal is to repeat
# if - check if it is true, then do a piece of code
# can use while instead of if (convoluted)

def my_log10(n):
    '''Return log10(n) for an n that is equal to a non-negative power of 10'''
    ans = 0
    cur_pow = 1
    while cur_pow < n: # 10^0 = 1
        ans = ans + 1
        cur_pow = cur_pow * 10
    return ans
    # if n = 1000, need to update ans 3 times (cur_pow = 1, 10, 100) for it to exceed n

if __name__ == "__main__":
    # print(my_pow(2, 3))
    # for1()
    # for2()
    # while1()

    if 3 < 5:
        print("3 is definitely smaller than 5")

    flag = True
    while flag and 3 < 5:
        print("3 is definitely smaller than 5")
        flag = False
    # same as using an if statement
    # if flag is not set to false, there will be an infinite loop

    # compute log10(n)
    # log10(100) = 3 because 10^3 = 1000

    print(my_log10(1000))















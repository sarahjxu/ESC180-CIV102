import math

def agree_with_pi(n):
    res = 0
    i = 0
    # equal = False
    pi_digits = int(math.pi*(10**(n-1)))
    while True: # equal == False:
        res = res + (-1)**i/(2*i+1)
        res_4 = int(res*4*(10**(n-1)))
        if res_4 == pi_digits:
            return i
        i+=1
    # return (i)

agree_with_pi(5)
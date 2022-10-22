def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    k = 2
    sqrt_n = int(n**.5)
    while k <= sqrt_n: # shell postmortem brings you to line 9...something wrong with while loop!
        if n % k == 0:
            return False
        k += 1 # this was the missing step!
    return True

def look_for_odd_prime(limit):
    for i in range(limit + 1):
        if is_prime(i) and i % 2 == 1:
            return i
    return None # don't really have to say this, if you don't return i and we reach the end of the function, then it will still return None
    # but better to be explicit
    # for nested for loops: return = exit function, break = exit this for loop

if __name__ == '__main__':
    print(is_prime(150))
    print(is_prime(151))

    # find the first odd prime number
    # just check numbers up to 100

    for i in range(101):
        if is_prime(i) and i % 2 == 1:
            break

    i = 0
    while i < 101 and (not(is_prime(i) and i % 2 == 1)):
        i += 1
    print(i)

    # the above return the same output, none are good. use a function
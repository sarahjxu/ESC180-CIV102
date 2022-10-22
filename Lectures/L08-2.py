# determine whether the input n is a prime number
# a prime number n is either 2 or is not divisible by any of 2.....n-1

def is_prime(n):
    '''Return True iff (if and only if) the non-negative integer n is prime'''
    # ie return return True if n is prime, False if it is not
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        # more efficient: in range(2, int(n**0.5)+1)
        # n % i is the remainder of the division of n by i
        # n is divisible by i iff n % i == 0
        if n % i == 0:
            return False
        # else:
            # return True
            # eg. 15 --> not divisible by 2, so don't return False...if you have else statement then it will return True. That is wrong as 15 is not prime.
    return True

def swap():
    # swap the values of a and b without using multiple assignment or a temporary variable
    # a, b = b, a

    a, b = 42, 43

    # a = a', b = b', a <- b', b <- a'

    a = a + b # a = a' + b', b = b'
    b = a - b # a = a' + b', b = a'
    a = a - b # a = b', b = a'

def fact(n):
    '''Return n! for a non-negative integer n'''
    res = 1
    # multiply res by 2, 3, 4....up to n
    for i in range(2, n+1): # up to and including n
        res *= i
    return res

def n_trailing_zeroes(n):
    n_fact = fact(n)
    while n_fact % 10 == 0:
        n_fact //= 10 # can't do /= 10...integer division too large for float. need to use //= division
        counter += 1


if __name__ == "__main__":
    print(fact(50))
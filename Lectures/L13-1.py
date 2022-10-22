def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def trailing_zeros_slow(n):
    fact_n = fact(n)
    res = 0
    while fact_n % 10 == 0:
        fact_n // 10
        res += 1
    return res
    # this takes verrrryyyyy long

# n! = 1*2*3*4*.....*n
#    = 10^k * ....
#    = 5^k * 2^m * ...
# 1 2 3 ... 5 ... 10 ... 15 ... 20 ... ... 125 ... ... 625
# (n//5) --> underestimated, 25 --> undercounting by 1, 125 --> undercounting by 2, etc.
# every 25 integers, undercount by 1 factor of 5
# every 125, undercount by 2
# (n//5) + (n//25) + (n//125) + (n//625) + ... 0

def trailing_zeros_fast(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
# approx number of dicisions: log_5(n)

if __name__ == "__main__":
    print(trailing_zeros_fast(200))

def gcd(n, m):
    if n > m:
        max = n
    else:
        max = m
    while max > 0:
        if n % max == 0 and m % max == 0:
            print(max)
            return
        max -= 1

gcd(8, 4)
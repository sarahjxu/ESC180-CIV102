def gcd(n, m):
    i = 1
    if n > m:
        max = n
    else:
        max = m
    while i <= max:
        remn = n % i
        remm = m % i
        if remn == 0 and remm == 0:
            div = i
        i += 1
    print(div)

gcd(278, 37)


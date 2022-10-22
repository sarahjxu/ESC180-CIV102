def simplify_fraction(n, m):
    # find the lowest divisor
    # divide each number with the divisor
    # if m = 1, just print n
    # if not, then print "n"/"m"
    if n > m:
        max = n
    else:
        max = m
    i = max
    while i > 0:
        remn = n % i
        remm = m % i
        if remn == 0 and remm == 0:
            div = i
            break
        i -= 1
    divn = n/div
    divm = m/div
    if divm == 1:
        print(int(divn))
    else:
        print(str(int(divn)) + "/" + str(int(divm)))

simplify_fraction(8, 4)
# python rounding - if it's 5, round to the nearest even number
# round(5.5) and round(6.5) both return 2
# division of an int by int is always a float
7/2 # gets you 3.5
6/2 # gets you 3.0

# integer diviision
7//2 # gets you 3
8//2 # gets you 4
-7//2 # gets you -4
2*(7//2)+1 == 7

# remainder (modulo)
7 % 2 # 7 mod 2, gets you 1
56 % 10 # gets you 6

# sign of the result is the same as the sign of the divisor
(-7) % 2 # 1
7 % (-2) # -1

2 * (-7//2) + (-7%2) == -7
# -7//2 set up such that the mod rule is valid (sign of mod is the same as the divisor)
# 2 * -4 + 1 == -7
# on files
# decimal numbers
# 231>10 = 2 x 10^2 + 3 x 10^1 + 1 x 10^0

# binary numbers
# 1101>2 = 1 x 2^3 + 1 x 2^2 + 0 x 2^1 + 1 x 2^0 = 8+4+1 = 13>10

# convert from decimal to binary
# 120>10 = 64 + 32 + 16 + 8
# highest power of 2 in 120 is 64
# highest power of 2 in 120 - 64 = 56 is 32
# 1 x 2^6 + 1 x 2^5 + 1 x 2^4 + 1 x 2^3 + 0 x 2^2 + 0 x 2^1 + 0 x 2^0
# 1111000

# in memory table
# 8 digit number is a bit
# 100000000 --> 2^8 = 256
# numbers between 0 and 255 can be represented with 8 binary digits
# 0: 0>2
# 1: 1>2
# 2: 10>2
# 3: 11>2
# long addition: 10+11 = 101
# 0 + 0 = 0
# 1 + 0 = 1
# 1 + 1 = 10
# 4: 100
# 5: 101
#...
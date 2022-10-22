L = [[1, 2], [3, 4]]
L1 = L # changing L1[0] is the same as changing L[0], same for L1[0][0]

L2 = [L[0], L[1]]

L2[0] = 3 # L2 is now [3, [3, 4], L is unchanged
L2[1][0] = 1 # L2 is now [3, [1, 4]], L and l1 are [[1, 2], [1, 4]]



# Global variables:
# Name            Address
# L               @1120
# L1              @1120
# L2              @1140

# Local variables (f)






# Memory
# Address          Value
# 1000             1
# 1020             2
# 1040             3
# 1060             4
# 1080             [@1000, @1020]
# 1100             [@1040, @1060] --> [@1000, @1060]
# 1120             [@1080, @1100] #L, L1
# 1140             [@1080, @1100] --> [@1040, @1100] #L2
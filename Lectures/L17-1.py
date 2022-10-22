# LHS = RHS
#1. If the RHS is a new object, put the object in memory first
#2. Assign the address of the object on the RHS to the LHS in the variable table
#3. If the LHS is an element of a list, change the memory table in the appropriate location

x = 600

L = [600]

L[0] = 500

L2 = L


# global variables
# Name              Address
# x                 @1020
# L                 @1040
# L2                @1040


# memory
# Address             Value
# 1000
# 1020                600
# 1040                [@1020]
# 1060                500
# 1080
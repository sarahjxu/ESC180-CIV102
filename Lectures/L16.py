a = "hello"
# taking "hello" and place it somewhere in memory, such as 1200

x = 500

y = x

id(a)
# query the address of a variable

for i in range(-10, 270):
    print(i, id(i))
# -5 up to 256 are preloaded as specific locations in memory when python starts out, other ones need to find random places to store it


# python will try to use the least memory possible
b = "hello"
print(id(a), id(b))
# same address, since they are the same, and we can't change the contents of a string (immutable)

c = "he"
d = "llo"
e = c + d
# not the same id, since for python to know c + d is also hello, need to run program, but need to store e somewhere before running program

L = [500, 501]
# L[0] = 501
# changing the contents of L --> python looks where L lives, then adjusts L[0]: [@1000, @1020] --> [@1020, @1020]

L2 = L
# not new variable, L2 is also @1040
L[0] = 501 # go into memory table and modify the first element of 1040 to @1020
# both L and L2 will now be [501, 501]
# aliasing: two variables referring to the same object
# L and L2 are aliases of each other

L2 = 500
# L doesn't care about this, we go into global variable table and change the address associated with L2 to @1000

# global variable table
# variable     address
# a            @1200
# x            @1000 #@: reminds us that 1000 is an address, python doesn't  store the @ --> it just knows it's an address
# y            @1000
# L            @1040
# L2           @1040


# memory table
# address    value
# 1000       500
# 1020       501
# 1040       [@1000, @1020]
# ...
# ...
# 1200       "hello"
# 1220
# get around 2^64 - 1 different locations (64 bit)
# voltage either high or low
# most values are just garbage values
# gap 1200-1220: doesn't take just one address for hello, takes multiple spaces, starting from 1200


# 3 rules:
# when we have an assignment operator (=)
# LHS = RHS
# 1. if RHS is a new object, place it in memory, then make LHS refer to the address of the new object in the global variable table
# 2. If LHS is a variable, make the address of LHS be the same as the address of RHS (in the variable table)
# 3. if LHS is an element of a list, make the content of the location in the memory table of the element equal to the address of the RHS
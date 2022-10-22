# boolean values and boolean algebra

# named after George Boole

b = True
a = False

if b:
    print("hi")
# the same as if b == True

if a:
    print("bye")
# if a == True

if not a:
    print("hello again")
# if not a == True

# but for better style,

want_to_print_hi = True

if want_to_print_hi:
    print("hii")

not want_to_print_hi

hate_to_print_hi = False
if not hate_to_print_hi:
    print("hiii")

# and
# if one or more of the operands in an and statement are false, then the whole statement is false
# True and True == True
# True and False == False
# False and True == False
# False and False == False

# or
# if at least one of the operands is true, then the whole statement is true
# True or True == True
# True or False == True
# False or True == True
# False or False == False

# for dessert, I'll have pie or ice cream, but not both

ice_cream = True
pie = False

if pie or ice_cream:
    # prints if both are true, which is wrong
    print("I didn't lie")

# method 1: list out all the possibilities
if (pie and not ice_cream) or (not pie and ice_cream):
    print("I didn't lie")

# method 2: is shorter --> all we want is one to be true, the other false
if pie != ice_cream:
    print("I didn't lie")
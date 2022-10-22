# functions
# f(x,y) = 2*x*y-5

def f(x,y):
    res = 2*x*y-5
    return res

# f --> function signature
# x, y --> parameters (variables you plug things into)
# 2, 5 --> arguments

def g(x,y):
    return 2*x*y-5

def prod(x,y):
    return x * y

def pirate_print(s):
    '''Print the piratified version of the string s
    ''' # docstring, like a comment
    print("Ahoy! " + s + " Arrgh!")
    # could use commas here

def piratify(s):
    '''Reutrn the piratified version of the sring s'''
    return "Ahoy!" + s + " Arrgh!"

def has_roots(a, b, c):
    '''Return True if a*x^2+bx+c has real roots'''
    disc = b**2-4*a*c
    return disc >= 0
    # compute discriminant, compute the value of disc >= 0
    # the value is True if disc >= 0, False if disc < 0

def fail_to_plunder_grade():
    grade = 67

def actually_plunder_grade():
    global grade # modifies the global variable grade. When referring to the variable grade, we mean the global variableS
    grade = 65

if __name__ == '__main__': # separator between function definitions and the main code block
#
    my_prod = prod(2,5) # just line doesn't do anything, cause you didn't tell it to print anything
    # sends 2 to x, 5 to y
    print(my_prod)
    print(f(2,5))
    pirate_print("I love CIV!") # string is sent to s, and the value of Ahoy, s, Arrgh is computed, and then the effect of print will print the value to the screen

    print(5, "hi") # prints multiple arguments
    # can't do print(5 + hi) since they are different types, need to do something extra for it to happen

    res = pirate_print("I love CIV!")
    print(res) #returns None
    # computes res --> prints I love CIV. Then the value of res is None. So then the print(res) prints None.

    piratify("I like Praxis <3!!!")
    # doesn't do anything, as it only stores Ahoy....Arrgh
    # need to print for it to ouput something
    print(piratify("I like Praxis <3!!!"))

    print(has_roots(5, 4, 3)) # False
    # print(disc)
    # error. disc is a local variable INSIDE the function, can't be accessed once has_roots() finishes running

    grade = 98
    fail_to_plunder_grade()
    print(grade)
    # prints 98. grade inside the function is a local variable, which means it won't be returned outside of it. grade outside of the function is a global variable

    actually_plunder_grade()
    print(grade)
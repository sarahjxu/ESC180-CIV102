import math # for sqrt
# need to import before using it...or else Python doesn't know what you're talking about

# Solve ax^2+bx+c = 0
# Print the values for which line 1 is true

# (x-2)(x+1) = x^2-x-2

a = 2
b = -20
c = 1

disc = b**2 - 4 * a * c # if you write 4ac, Python thinks ac is a variable
# disc is a float (with decimal points)

if disc > 0:
    r1 = (-b+math.sqrt(disc))/(2*a)
    r2 = (-b-math.sqrt(disc))/(2*a)
    print(r1, r2)
elif disc == 0:
    r = -b/(2*a)
    print(r)
else:
    print("no solutions")

x = 9.949747468305834
print(a*x**2+b*x+c)

# get something very close to 0
# the function is continuous
# if not continuous, approximation of root, f(x) could be anything
# could there be an exact value for x? so that when we plug it back we get 0 and not very close to 0
# irrational number - computer only stores finite sequences, can't compute all of the irrational number
# eg. math.pi --> 3.141592653589793
# most irrational numbers are transcendental, can't express them algebraically

x = 9.949747468305834
print((a*x**2+b*x+c - a*r1**2+b*r1+c) == 0)
# prints true

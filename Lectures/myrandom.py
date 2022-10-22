def myrandom():
    global x
    # seed(x)
    x = (a * x + b) % m
    return x/m

def seed(s):
    global x
    x = (a * s + b) % m # don't want when seeded with 0, get 0 back

a = 1664525
b = 1013905223
m = 2**32
x = 0
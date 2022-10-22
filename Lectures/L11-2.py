import random

random.seed(0)
# set the seed to 0, so every time I run always start from the first "random" in the funtion

random.random() # a pseudo-random number between 0 and 1 (not including 1)

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
# x, f(x), f(f(x)), f(f(f(x))) ... gives you a sequence where the numbers will appear as random

(p1 * x) % p2
p1 = 209348593832
p2 = 293867
x = 23984279847
x = (p1 * x) % p2 # congruence
print(x/p2)
# a pseudo random function

N = 100000
count = 0
for i in range(N):
    x, y = random.random(), random.random()
    if x**2 + y**2 < 1:
        count += 1
        # count is the number of points in the quarter circle, N is the number of points in the square

print("Approximation of pi:", 4*count/N)
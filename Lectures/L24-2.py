import time
import random

t0 = time.time() # which timezone? UTC-0 time

# t1-t0: number of seconds elapsed between when you computed t0 and t1

N = 100000
s = 0.0
a = 0
for i in range(N): # 2: increment counter, put it in i
    s += random.random() # 7: random.random --> ((ax+b)%m)/m for a number between 0 and 1
# *, +, %, take central digits, /, +, =
# total: 9 elementary operations

    a += s # now its 11, should add 22% of time

t1 = time.time()


print(1000*(t1-t0)/N, " ms per iteration")
print(1000*((t1-t0)/N)/9, " ms per iteration")
import random

def longest_run1(s, c):
    run = 0
    max_run = 0

    if c == "z":
        s += "y"
    else:
        s += "z"

    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else:
            run += 1

    return max_run




def longest_run2(s, ch):
    for longest in range(len(s), -1, -1):
        if ch*longest in s:
            return longest

    return 0


def longest_run3(s, ch):
    for longest in range(len(s), -1, -1):
        cur_run = 0

        for i in range(len(s)):
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0

            if cur_run == longest:
                return longest
    return 0


def gen_ab(length):
    s = ""
    for i in range(length):
        if random.random() > 0.5:
            s += "a"
        else:
            s += "b"
    return s

lengths = [10, 100, 500, 1000, 1500, 2000, 5000, 10000, 100000, 200000, 400000, 1000000]
lengths = lengths[:8]

runtimes1 = []
runtimes2 = []
runtimes3 = []

import timeit

for length in lengths:
    s = gen_ab(length)
    runtimes1.append(timeit.timeit("longest_run1(s, 'b')", number = 3, globals = globals()))
    runtimes2.append(timeit.timeit("longest_run2(s, 'b')", number = 3, globals = globals()))
    runtimes3.append(timeit.timeit("longest_run3(s, 'b')", number = 3, globals = globals()))


import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(lengths[:8], runtimes1[:8])
plt.plot(lengths[:8], runtimes2[:8])
plt.plot(lengths[:8], runtimes3[:8])
plt.xlabel("len(s)")
plt.ylabel("runtime(sec)")
plt.yscale("log")
plt.xscale("log")
plt.show()
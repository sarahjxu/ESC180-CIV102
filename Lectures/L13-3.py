# nested loops
counter = 0
for i in range(5):
    for j in range(3):
        print(counter, "i = ", i, "j = ", j)
        counter += 1


# "unrolling the loop"
# don't do it unless you know what you're doing
# this is the same as the nested loop

counter = 0
i = 0
for j in range(3):
    print(counter, "i = ", i, "j = ", j)
    counter += 1
i = 1
for j in range(3):
    print(counter, "i = ", i, "j = ", j)
    counter += 1
# ...
i = 4
for j in range(3):
    print(counter, "i = ", i, "j = ", j)
    counter += 1


# this is also the same
def count_to_k(k, i, counter):
    for j in range(k):
        print(counter, "i = ", i, "j = ", j)
        counter += 1
    return counter

for in in range(5):
    counter = count_to_k(3, i, counter)
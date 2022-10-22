# infinite loops

while True:
    print("Praxis!!!")
    # no break condition

# break, continue
# usually advise you to avoid them, try to make early return or rewrite so you don't need them

# break: exit the loop, go to the next line
for i in range(5):
    if i == 3:
        break
    print(i)

print("hi")

# contine: exit the current iteration, and go to the next one

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)
# this is not ideal!

for i in range(1, 5, 2):
    print(i)
# this is much better!

for i in range(5):
    if i % 2 != 0:
        print(i)
# this is even better than lines 20-23
# try not to use continue, sometimes continue creates problems

i = 0
while i < 5:
    if i % 2 == 0: # this part creates an infinite loop...start at 0, continue, never increment. add i += 1 inside if
        continue
    print(i)
    i += 1

i = 0
while i < 5:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1
    if (i-1) % 2 == 0:
        continue
    print(i-1)

# only use continue when you have an exception in the middle of the loop, but you aren't sure how the rest of the loop will work
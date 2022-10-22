# lists
earnings = [86, 63, 68, 69]

earnings[0] # 86
# list indicies start at 0

len(earnings) # shows the number of elements in the list

# last element in the list
earnings[-1]
earnings[len(earnings)-1]

earnings[-2]
earnings[len(earnings)-2]

for e in earnings:
    print(e)
# goes through earnings and puts element 1 in e, element 2 in e...

USD_TO_CAD = 1.4
for e in earnings:
    print(e * USD_TO_CAD)
    # prints 120.39999999999 etc, since in binary 1.4 is 1.4000000000 (infinite series)
    e = 0 # this has no effect! we put the values of earnings into e, so even if you make e = 0, it doesn't do anything to the loop or to the array

for i in range(len(earnings)):
    earnings[i] *= USD_TO_CAD

# to access elements in list - use e in earnings
# to change the values of elements in the list, or use element i and it's neighbours - use i in range

# write a function that returns True iff the list L is not decreasing
# for every i between 1 and len(L)-1, L[i] >= L[i-1]
# eg. [1, 2, 2, 5, 6, 6, 7]: non-decreasing
# eg. [1, 2, -1, 5, 6, 5, 8]: not non-decreasing

def is_non_decreasing(L):
    for i in range(1, len(L)): # start at 1 to compare pairs
        if L[i] < L[i - 1]:
            return False
    return True
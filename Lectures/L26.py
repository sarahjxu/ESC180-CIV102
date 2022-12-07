def find_max_i(L):
    '''return the location of max(L) inside L'''
    cur_max = L[0]
    cur_max_i = 0
    for i in range(1, len(L)):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_i = i
    return i

# what is the tight upper bound on the asymptotic runtime complexity of find_max_i, in terms of the length of L?
# O(n), where n = len(L)
    # in the worst case
    # but this case has no best/worst case, must run to the end to confirm max

# want 10^res = n
# n = 1000, res = 0
# n = 100, res = 1
# n = 10, res = 2
# n = 1, res = 3
def log10(n):
    res = 0
    while n > 1:
        n /= 10
        res += 1
    return res

# runtime complexity: # times that the while loop repeats (res times)
# assuming that arithmetic operations take O(1) time, the complexity of log10 is O(log n)
# if n or res are VERY LARGE, then operations take a long time (for integers)
# but on exam, assume n is a float, which limits the floating points, and it is TRUE that the time for operations remains constant

# log_10(n) = log(n)/log(10)

def quadratic(L):
    for i in range(len(L)):
        for j in range(len(L)//2):
            pass
    # in total, the loop runs n*(n/2) times

# complexity O(n^2), n = len(L)

def find_i(L, e):
    '''return the index of i in e'''
    for i in range(len(L)):
        if L[i] == e:
            return i

# complexity  O(n), in the worst case it will run n times

# L = [1, 5, 6, 10, 20, 56, 60, 400]
# index of 5?
# is 5 in the first half of the list? Yes
# is 5 in the first quarter of the list? Yes
# is 5 in the first eigth of the list? Yes

# 1 million possibilities
# 500k (eliminate half by asking a question)
# 250k
# 125k
# ..
# .
# ~log2(1e6) questions needed

# 1e6
# ...
# 4
# 2
# 1 possibility
# 2^k = 1e6
# k ~ 20


# L = [1, 5, 6, 10, 20, 56, 60, 400]
# e = 5
# low = 0
# high = 7
# mid = 3

# low = 0
# high = 2
# mid = 1
# return 1

# e = 56
# low = 0
# high = 7
# mid = 3

# low = 4
# high = 7
# mid = 5
# return 5

def find_i_binary(L, e):
    '''return the location of e in list L, return None if e is not in L,
    assume L is a sorted list of floats'''
    low = 0
    high = len(L) - 1
    # Make sure the if e is in L, its location is between low and high
    while high - low >= 2:
        mid = (low + high)//2
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return mid
    # it must be that high - low < 2
    if L[low] == e:
        return low
    if L[high] == e:
        return high
    else:
        return None

# in the worst case, e is not in L
# keep track of how high-low changes
# every iteration, high-low decreases by at least a factor of 2
# n = high-low
# n/2 = high-low
# n/4 = high-low
# ...
# 1 = high-low
# approx log2(n) iterations to get from n to 1 by dividing by 2 every time
# O(log(n)) time for n = len(L)
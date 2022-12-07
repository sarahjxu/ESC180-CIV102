# total runtime: k3 + (k1+k2)*n, which is O(n)
def longest_run1(s, c):
    # n = len(s)
    run = 0
    max_run = 0

    if c == "z":
        s += "y" # runtime: k1*n for some constant k1
    else:
        s += "z"

    # runtime: k2*n for some constant k2
    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else:
            run += 1 # assume consant time (literally true for floats, not for ints)
    # float addition: always the same size, takes the same amount of time

    return max_run




def longest_run2(s, ch):
    for longest in range(len(s), -1, -1):
        if ch*longest in s:
            return longest

    return 0 #Optional, 0 will be returned anyway since '' is in any string


def longest_run2(s, ch):
    # n*(k1*n) time, which is O(n^2)
    for longest in range(len(s), -1, -1):
        cur_run = 0

        # k1*n time
        for i in range(len(s)):
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0

            if cur_run == longest:
                return longest
    return 0
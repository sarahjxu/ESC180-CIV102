# state variables

# "xaaaabaabbaab" n = 2

def n_as_plus_b(s, n):
    query = "a" * n + b
    s = "x" + s + "x"
    # no situation where a is the first character or b is the last
    if query in s:
        loc = s.find(query)
        if s[loc + len(query)] != "b" and s[loc-1] != "a":
            return True
        s = s[loc+len(query):]
    return False


# "aaaabaabbaab"
def n_as_plus_b1(s, n):
    cur_run_a = 0
    for i in range(len(s)):
        if s[i] == "a":
            cur_run_a += 1
        else:
            if s[i] == "b":
                if cur_run_a == n:
                    if i == len(s)-1:
                        return True
                    if s[i+1] != "b":
                        return True
            cur_run_a = 0
    return False
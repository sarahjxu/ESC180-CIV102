# longest run of the single-character string c in the string s

# s = "abbaaaac" c = "a": longest run is 4
# s = "abbaaaac" c = "b": longest run is 2

def longest_run(s, c):
    for i in range(len(s), -1, -1):
        if c * i in s: # have a run of i c's, starting from largest instead of smallest i
        # empty string is always inside s
        # "" in s --> True
            return i

def longest_run2(s, c):
    # state variables --> use them for the structure of code, so if you want to prove that the code is mathematically correct, you can just do a proof by induction
    # induction: I set the variables correctly for 0, inductive step is that they will also work for n and n + 1
    run = 0 # length of the current run
    max_run = 0 # the longest run
    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else:
            run += 1
    # return max_run
    # doesn't update the last letter!
    # since we don't get to the point where ch != c with the last run, since there's no letters let and we don't go back to that loop.
    # so need to max the last run and the alst updated max_run
    return max(run, max_run)
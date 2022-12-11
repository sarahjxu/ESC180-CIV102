# alphabet = "abcdef"
'''generate all strings of a certain length as passwords'''

'''for c1 in alphabet:
    for c2 in alphabet:
        ...
        the dumb way'''

# [rint all stings of length n over alphabet alphabet

def print_all(alphabet, n, str = ""):
    '''printall strings over alphabet alphabet of lnegth n,
    pre-pend the string start_str to every str'''

    if n == 0:
        print(start_str)
        return

    for letter in alphabet:
        '''a [all combinations
            ...
            ...
            ...
            ]
            b [all combinations...'''

        print_all(alphabet, n-1, start_str + letter)

# k = len(alphabet)

# [0, "aaaa"] [0, "aaab"] ...                                    # k^n calls (there are n+1 levels)
#     [1, "aaa"]  [1, "aab"], [1, "aac"]                         # k^3 calls
#        [2, "aa"] [2, "ab"] [2, "ac"]                           # k^2 calls (each k calls k calls)
#               [3, "a"]                     [3, "b"] [3, "c"]   # k calls
#                        [4, ""]                                 # 1 call
# alphabet: "abc", n = 4

# complexity?
# print all does the same amount of work, so how many calls?
# 1 + k + k^2 + ... + k^n calls = (k^(n+1)-1)/(k-1) calls in total. Approx k^n calls
# O(k^n), approximately

def all_combinations(alphabet, n, start_str = ""):
    '''Return a list of all strings over alphabet alphabet, of length n, with start_str pre-pended'''

    if n == 0: #base case
        return [start_str]

    res = []
    for letter in alphabet:
        res.extend(all_combinations(alphabet, n-1, start_str+letter)) # add all the strings starting with a, b, c...etc.
        # make problem smaller by giving it the start_str, which increases to hold a, aa, aaa....etc.
        # use extend instead of append, since L.append([2, 3]) for L = [1, 2] gives you [1, 2, [2, 3]] while L.extend([2, 3]) gives [1, 2, 2, 3] which is what you want
    return res


# given string s, return True if s contains "a*n + b", with no trailing b's
# n_as_plus_b(("xxxaaab", 3) --> True
# n_as_plus_b(("xxxaaabx", 3) --> True
# n_as_plus_b(("xxxaaabb", 3) --> False
# n_as_plus_b(("xxxaaaab", 3) --> False

def n_as_plus_b(s, n):
    query = n*"a" + "b"
    query += "a"
    while query in s:
        if s.find(query)+len(query) != "b":
            return True
        s = s[s.find(query)+len(query):] # make new string start with the next character
        #for cases like this: "aaabbaaab"
    return False
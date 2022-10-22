# an anagram of s1 is a string with the same letters as s2, but in possibly different order and possibly a different number of spaces
# capitalization doesn't matter

# "Praxis forever" and "A prefix rovers" are anagrams

"abbbcc".count("ab") # returns 1
"abbbcc".count("c") # returns 2
"a".isalpha() # True
"@".isalpha() # False

s1 = "Praxis forever"
s2 = "A prefix rovers"

def is_anagram(s1, s2):
    '''return True iff s1 and s2 are anagrams'''
    s1 = s1.lower()
    s2 = s2.lower()
    for c in s1 + s2:
        if c.isalpha():
            if s1.count(c) != s2.count(c):
                return False
    return True

def is_anagram2(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    if sorted(s1) == sorted(s2):
        return True
    return False
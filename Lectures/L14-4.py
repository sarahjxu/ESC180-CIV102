# reverse a string
s = "praxis"

def reverse_str1(s):
    return s[::-1]

def reverse_str2(s):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

def reverse_str3(s):
    res = ""
    for c in s:
        res = c + res
    return res

print(reverse_str1(s), reverse_str2(s), reverse_str3(s))
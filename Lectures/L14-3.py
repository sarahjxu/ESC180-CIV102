s = "antidisestablishmentarianism"

print(s[6])
print(s[:4])

a = s.index("i")
b = s.find("i")
i = s.find("z")
s[i]

print(a, b, i, s[i])

s1 = s.replace("anti", "pro")
s = s.replace("anti", "pro")
s = 5
# strings are immutable, you can't actually CHANGE the string/the contents of the string

s.capitalize()

def my_capitalize(s):
    s = s.capitalize

def my_capitalize(s):
    return s.capitalize()

if __name__ == "__main__":
    s = "antidisestablishmentarianism"
    s = my_capitalize(s)
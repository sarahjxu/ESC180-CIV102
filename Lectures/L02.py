# conditionals "if-statements"
# compute |n|, the absolute value of n and print it

n = -4

if n <= 0: # boolean --> either true or false that n <= 0
    print(-n)
    print("Converted a non-positive to a non-negative")
else:
    print(n)

print("done") # this line is printed either way since it's after the if/else (no indentation)

grade = 98

# checks code from top to bottom, if the if statement is true, directly print, don't check anything below
# else, go down to the next statement and check for true/false. If true, then print, don't check anything below
# etc.
if grade >= 99:
    print("wheeee")
elif grade >= 95:
    print("ok")
elif grade >= 92:
    print("meh")
else:
    print("yikes")

# ORDER MATTERS
# with this code, for grade = 100, it will say "meh", since that's the first statement it sees and the statement is correct
if grade >= 92:
    print("meh")
elif grade >= 95:
    print("ok")
elif grade >= 98:
    print("wheeee")
else:
    print("yikes")
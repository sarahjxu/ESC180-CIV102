a = 2
if a > 5:
    print(">5")
elif a > 1:
    print(">3")
else:
    print("else")

# order matters - the first statement in if/else should be the strictest/most restricted conditional...if that's what you want to do
# prints >3 ONLY

a = 10
if a > 5:
    print(">5") # no else here. lines 12-13 stand on their own. it is separate from the conditionals of 14-17
if a > 1: # lines 14-17 is one block of code that is being evaluated
    print(">3")
else:
    print("else")

# prints >5 AND >3

# order only matters when you're using ranges of values...if you're looking at specific values for the conditionals, it doesn't matter as much

b = 5
if a == 'hi':
    print("hi")
elif a == "hello":
    print("hello")
elif a == "hi" and b == 5: # this line will not run, if a = "hi", as the IF line will run first...needs order here!
    print("help")
elif a == "hi" or b == 5: # if you reach this line, then a cannot be hi...or else the IF line would run. Only useful in terms of b = 5
    print("weird")
else:
    print("end")

# string literals --> anything you put into python that has a value
# eg. 123 is just a literal, "hi" is a string literal, 4.5 is a literal (floating-point number)
123 #an integer
"hi"
4.5
"234*475(#4%(**"
a23424 # identifier - name of a variable/function
3a345 # an error - not a valid identifier, not a valid literal of any kind

# on the differences between single and double quotes:
s = 'Artscis are "smart"' # this is valid
# s = "Artscis are "smart"" is NOT valid
# Python reads left to right --> reads "Artscis are " as a string, and then smart following that
# can't have this follow without a connector
# single quotes can go into double, double can go into single, no double quotes can go into double quotes
smart = "silly"
s = "Artscis are " + smart # this is valid
# OR add \ to tell Python you mean a "" inside a string, not separating strings
s = "Artscis are \"smart\""
# what if I want a backslash?
s = "\\" # here comes a slash I want to store inside the string

"abc
def
ghi"
# this is wrong!!

# multi-line comments
'''
test
yay
it works
'''

a = '''abc
def
gh'''
print(a)
# also printable

d = "12\n34"
print(d)
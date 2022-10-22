# variable types
# int (integer): a whole number, unlimited in size
    # a = 5
    # type(a) --> int
# float: floating-point number
# str: string (a character string)
    # single quotes and double quotes both work
# functions

def f():
    return 2

# converting between different types:
str(42) # "42"
# can't say "a" + 42
# error: trying to add strings and integers
"a" + str(42) # this one works!

str(3.14159)

print("The prefix of the course code is " + "ESC" + " and the number is " + str(180))
print("ESC", 180) # adds a space between the two
print("ESC", 180, sep = "") # removes the space
print("ESC", 180, "adf", sep = "!!!!")

# convert between integer and float
float(5) # 5.0
int(5.0) # 5
int(6.8) # 6
# here python does truncation. the fractional part gets taken away...not actually rounding down
int(-6.8) #-6 --> this is rounding up
round(6.8)

# python convention
a = 7.8
int(a) # 7
int(a + 0.5) # 8
# if a is between 7.0 and 7.5, adding 0.5 still makes it 7 after truncation
# if a is between 7.5 and 8.0, adding 0.5 makes it 8, so it truncates to 8
# but this works for positive numbers
# for neg, subtract 0.5 for the same rounding effect
a = int(a + 0.5) # this changes the value of a. just int(a + 0.5) creates a new value, but doesn't change a

# int("3.14")
# doesn't work since 3.14 is not an int
int(3) # this one works
# can convernt 3.14 to float
float("3.14")
int(float("3.14")) # this one works too
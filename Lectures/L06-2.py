# naming variables and functions

# a valid name for a variable or function starts with a letter or an underscore _ and contains only letters, numbers and underscores

'''5skdjfhsk = 5 ''' # this is illegal
# python reads the 5 and thinks it's not a variable/function, thinks its a number...but it's not

_asldjalskjd1232424 = 5 # immoral
a = "ESC180" # jaywalking, name doesn't reflect the purpose of the variable

# pothole case
num_courses_engsci = 6

# guidelines:
# make it meaningful
# separate words (or abbreviations) with underscores
# all-lowercase

# to indicate that you're referring to a constant, can use all-caps
PI = 3.141592653589793
PI = 3
# not a constraint on python, just for when you're writing code, you know you shouldn't modify all-caps, even though python doesn't have a problem with it

# camelcase is fine...but usually python uses pothole case
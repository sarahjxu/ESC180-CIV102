# dictionaries

user = ["guerzhoy", "cluett", "stangeby"]
password = ["asdfa", "matrix", "rigorous"]

# define a dictionary
# an unorded set of key-value pairs
# "guerzhoy" --> key, "asdfa" --> value
# keys are unique, values can repeat
passwords = {"guerzhoy":"asdfa", "cluett":"matrix", "guerzhoy1":"asdfa"}

passwords["guerzhoy"]

passwords["davis"] = "integral"

passwords[99] = [1, 2, 3]
# doesn't have to be strings!

# JUST CANNOT BE MUTABLE

# passwords[[1, 2]] = 5 --> error, key has to be immutable

passwords[(1, 2)] = 5
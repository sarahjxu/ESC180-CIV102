def drop_courses_bad(grades):
    for course, grade in grades.items():
        if grade < 91:
            del grades[course]
    return grades
# no problem of global local - grades is an alias of whatever we send in, and we are just modifying ???
# bad, changed dict size while using it --> like with lists

def drop_courses_ok(grades):
    for course, grade in list(grades.items()):
        if grade < 91:
            del grades[course]
    return grades
    # going through the copy of the original dictionary, modifying the original dictionary
    # doesn't create problems since the grades are unique

def drop_courses_good(grades):
    res = {}
    for course, grade in grades.items():
        if grade >= 91:
            res[course] = grade
    return res
    # not problematic, building a new dictionary, not changing the contents of the original dictionary

grades = {"180": 90, "103": 91, "CIV": 90}


# clear the dictionary grades --> make it empty
grades.clear() # gives you {}

def manual_clear_bad(d):
    for k in d:
        del k[d]
    return d
    # modifying dict while going through it, bad

def manual_clear_ok(d):
    for k in list(d.keys()):
        del d[k]
    return d

def manual_clear_while(d):
    while len(d) > 0:
        # get SOME key from dict and delete it
        # grades.keys()[0] --> error
        # list(grades.keys())[0] --> works
        del d[list(d.keys())[0]]
    return d

def clear_bad_local(d):
    d = {}
    # place empty dict into {}, change local d to {}, no effect on the d outside the function
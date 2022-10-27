# get all the courses in which I got the grade grade

grades = {"180": 90, "103": 91, "CIV": 90}

def get_courses_bygrade(grades, grade):
    res = []
    for course, gr in grades.items():
        # check every entry whether gr matches grade
        if gr == grade:
            res.append(course)
    return res

a = get_courses_bygrade(grades, 90)
print(a)

# invert a dictionary d
# in the output: the keys are the values of d, and the values are the lists of the keys that correspond to them

inv_grades = {90: ["180", "CIV"], 91: ["103"]}

def inv_dict(d):
    res = {}
    for k, v in d.items():
        # start k, v = "180", 90
        # check if k in res: no
        # so then make key 90 which contains k
        # check "103" and 91
        # make dict element with key 91 containing 103
        # check "CIV" and 90
        # have 90, so then add value "CIV" to 90
        if v in res:
            res[v].append(k)
            # res[90] is ["180", "CIV"]
        else:
            res[v] = [k]
    return res

# 90 in grades --> False
# "180" in grades --> True
# 4 in [1, 2, 4, 4] --> True

b = inv_dict(grades)
print(b)
L = [2.3, 3.9, 4.0, 4.0, 1.3, 2.3]
# remove first 4.0?
L[2:3] = []
L[2:3] = [4, 5, 6]

L = [2.3, 3.9, 4.0, 4.0, 1.3, 2.3]
del L[2]

def drop_course_bad(grades):
    for i in range(len(grades)):
        if grades[i] < 4.0:
            del grades[i]
    return grades
    # list index out of range...it's using the original length of grades...but we're deleting elements from grades so you get error when indexing out of the list grades

def drop_course_bad1(grades):
    i = 0
    while i < len(grades):
        if grades[i] < 4.0:
            del grades[i]
        i += 1
    return grades
    # this one skips values...since after element at 0, we increment, and then it doesn't check the new element 0

def drop_course_good(grades):
    i = 0
    while i < len(grades):
        if grades[i] < 4.0:
            del grades[i]
        else:
            i += 1
    return grades

def drop_course_good1(grades):  # THIS IS THE OPTIMAL WAY
    res = []
    for grade in grades:
        if grade >= 4.0:
            res.append(grade)
    return res

grades = [2.3, 3.9, 4.0, 4.0, 1.3, 2.3]

# IN GENERAL: it's a bad idea to go over a list while modifying it
# it's better to build a new list than trying to change the original list while using it as a parameter
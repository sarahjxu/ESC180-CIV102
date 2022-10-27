grades = {"180": 90, "103": 91, "CIV": 90}
# 180, 103, CIV are keys that are unique and immutable (strings, integers, tuples)
# cannot be lists

grades["180"]
# must get a definite thing, can't get 2 entries for it

grades[50] = 123
# more flexible than lists, for lists you need to make sure there is space for an index at 50

grades.keys()
# get all keys --> gives you object like list, but not a list
list(grades.keys())[2]
# don't rely on this to find the corresponding value @ 2 --> may not be ordered in the way you inputed them

grades.values()

grades.items()
# tuples that contain key value pairs

list(grades.items())[1]

#unpacking the tuple...
coords, value = list(grades.items())[1]
list(grades.items())[0][1] # 90

# for k, v in grades.items():
    # print(k, v)
    # don't want grades.items() to be a new thing --> if it is very large, then you are copying everything (list)
    # an object that keeps track of which tuples it gave you already, and which it should give you next

# for k, v in list(grades.items()): # this will take a lot of memory if dictionary is very large
    # print(k, v)

for course, grade in grades.items():
    print(course, grade)

for course in grades: # does the same thing as the loop above
    print(course) # gives you keys
    print(course, grades[course])

for course in grades.keys():
    print(course, grades[course]) # not the convention

# get all the courses in which I got the grade grade
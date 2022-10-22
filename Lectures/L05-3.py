def adjust_grade():
    global grade
    grade = grade + 3

def adjust_grade2():
    return grade + 3 # defaults to the global variable

def adjust_grade3(grade):
    return grade + 3

def adjust_grade4(grade):
    grade = grade + 100 # operating on the local variable
    return grade - 97 # the only thing that matters is the return value, when something is equal to the return value. local variable changes don't matter until they reflect in the return statement

def adjust_grade5(g): # all we did was rename the local variable. still prints the same thing as adjust_grade4
    g = g + 100
    return g - 97

def adjust_grade_error():
    grade = grade - 5 # did not say global grade, but there's no local variable grade. So that means it should be global grade. But then since you didn't say global grade, then it SHOULD be local
    # python produces error

def adjust_grade_error_2():
    global grade
    grade = 5
    # grade is both parameter (local) and global --> inconsistent!

if __name__ == '__main__':
    grade = 92
    adjust_grade() # grade is 95
    grade = 92
    adjust_grade2() # grade is still 92
    # the value of adjust_grade2 is 95
    # but we didn't actually change grade
    # but if we do this...
    grade = adjust_grade2() # grade is now 95
    grade = 92
    grade = adjust_grade3(grade) # grade is now 95
    grade = 92
    grade = adjust_grade4(grade)
    grade = 92
    grade = adjust_grade5(grade)

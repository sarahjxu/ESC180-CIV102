'''code = a = 5
print(a)

exec(code)'''

def make_code_that_prints_n(n):
    return "print(" + str(n) + ")"

if __name__ == "__main__":
    code = make_code_that_prints_n(60)
    exec(code)
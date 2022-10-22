# s = "abcdef"

# for c1 in s:
#     for c2 in s:
#         for c3 in s:
#             print(c1+c2+c3)

code = '''a = 5
print("a\a")'''

exec(code)

#f-string
x = 12
f"the value of x is {x}"

def gen_nested_loop(n):
    res = "def gen_passwords(alphabet):\n"
    for i in range(n):
        res += f"{(i+1)*' '}for letter{i} in alphabet:\n"
    add_line = "password = "
    for i in range(n):
        add_line += f"letter{i} + "
    add_line += "''\n"
    res += f"{' '*(n+1)}{add_line}"
    res += f"{' '*(n+1)}print(password)\n"

if __name__ == '__main__':
    code_15 = gen_nested_loop(15)
    exec(code_15)
    gen_passwords("abcdefgh")
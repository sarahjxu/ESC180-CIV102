'''text = open("data2.txt", "r")

lines = len(text.readline())

text = open("data2.txt", "r")

for i in range(lines):
    read_line = text.readline()
    lowered_line = read_line.lower()
    find_lol = lowered_line.find("lol")
    if find_lol > -1:
        read_line.strip("\n")
        print(read_line)'''

text = open("data2.txt", "r")

lines = text.readlines()

for i in range(len(lines)):
    # read_line = text.readline()
    lowered_line = lines[i].lower()
    find_lol = lowered_line.find("lol")
    find_n = lowered_line.find("\n")
    if find_n > -1 and find_lol > -1:
        print(lines[i][:-1])
    elif find_lol > -1:
        print(str(lines[i]))
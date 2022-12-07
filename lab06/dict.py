def dict_to_str(d):
    string = ""
    count = 0
    for key, val in d.items():
        string += str(key) + ", " + str(val)
        count += 1
        if count < len(d):
            string += "\n"
    print(string)

def dict_to_str_sorted(d):
    sorted = []
    string = ""
    count = 0
    for key in d.items():
        sorted.append(key)
    sorted.sort()
    for key in sorted:
        k, v = key
        string += str(k) + ", " + str(v)
        count += 1
        if count < len(d):
            string += "\n"
    print(string)

dict_to_str({1:2, 5:6})
dict_to_str_sorted({1:2, 0:3, 10:5})
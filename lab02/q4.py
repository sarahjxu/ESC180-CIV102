def display_current_value():
    print("Current value: " + str(value))

def add(to_add):
    global value
    value = to_add + value

if __name__ == "__main__":
    print("Welcome to the calculator program.\nCurrent value: 0")
    value = 5
    to_add = 4
    add(to_add)
    display_current_value()
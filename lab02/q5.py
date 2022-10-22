def display_current_value():
    print("Current value: " + str(value))

def add(to_add):
    global value
    value = to_add + value

def mult(to_mult):
    global value
    value = to_mult * value

if __name__ == "__main__":
    print("Welcome to the calculator program.\nCurrent value: 0")
    value = 5
    to_mult = 4
    mult(to_mult)
    display_current_value()
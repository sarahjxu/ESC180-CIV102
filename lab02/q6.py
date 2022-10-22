def display_current_value():
    print("Current value: " + str(value))

def add(to_add):
    global value
    value = to_add + value

def mult(to_mult):
    global value
    value = to_mult * value

def div(to_div):
    global value
    value = value / to_div

if __name__ == "__main__":
    print("Welcome to the calculator program.\nCurrent value: 0")
    value = 20
    to_div = 4
    div(to_div)
    display_current_value()
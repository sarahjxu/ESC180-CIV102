def display_current_value():
    print("Current value: " + str(value))

def administrative():
    global undo_values
    global count1
    undo_values.append(value)
    count1+=1
    display_current_value()

def add(to_add):
    global value
    value = to_add + value
    administrative()

def mult(to_mult):
    global value
    value = to_mult * value
    administrative()

def div(to_div):
    global value
    value = value / to_div
    administrative()

def undo():
    global count1
    global value
    count1 = count1 - 1
    value = undo_values[count1]
    count1 += 1
    display_current_value()

if __name__ == "__main__":
    print("Welcome to the calculator program.\nCurrent value: 0")
    undo_values = []
    count1 = 0
    if_continue = True
    value = int(input("Input a value: "))
    undo_values.append(value)
    while if_continue == True:
        function = input("Select a function (add, mult, div, mem, recall, undo, quit): ")
        if function == 'add':
            to_add = int(input("Input number to add to " + str(value) + ": "))
            add(to_add)
        elif function == 'mult':
            to_mult = int(input("Input number to multiply with " + str(value) + ": "))
            mult(to_mult)
        elif function == 'div':
            to_div = int(input("Input number to divide " + str(value) + " by: "))
            div(to_div)
        elif function == 'undo':
            undo()
        elif function == 'quit':
            if_continue = False
        else:
            print("Invalid function")
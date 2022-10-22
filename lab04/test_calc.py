import lab02

if __name__ == '__main__':
    lab02.initialize()
    lab02.add(42)
    if lab02.get_current_value() == 42:
        print("Test 1 passed")
    else:
        print("Test 1 failed")
    lab02.add(0)
    if lab02.get_current_value() == 42:
        print("Test 2 passed")
    else:
        print("Test 2 failed")
    lab02.divide(0)
    if lab02.get_current_value() == "ERROR":
        print("Test 3 passed")
    else:
        print("Test 3 failed")
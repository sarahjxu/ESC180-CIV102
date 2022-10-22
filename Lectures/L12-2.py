def login(username, password):
    global attempted_logins, locked
    if locked:
        return False
    if username not in usernames:
        attempted_logins += 1
        if attempted_logins == 3:
            locked = True
        return False
    if passwords[usernames.index(username)] == password:
        attempted_logins = 0
        return True
    else:
        attempted_logins += 1
        if attempted_logins == 3:
            locked = True
        return False

def initialize():
    global attempted_logins, locked, usernames, passwords
    locked = False
    attempted_logins = 0
    usernames = ["guerzhoy", "cluett", "stangeby"]
    passwords = ["ILovePython", "matrix", "rigorous"]
# use initialize instead of putting in main block for when you import it, so that it will actually run
# stuff in the main block does not run after you import

initialize()

if __name__ == "__main__":
    initialize()
    print(login("stangeby", "rigorous"))
    print(login("guerzhoy", "pythonismeh"))
    print(login("guerzhoy", "pythonismeh"))
    print(login("guerzhoy", "pythonismeh"))
    print(login("stangeby", "rigorous"))
    # after 3 failed logins, the successful one fails as well

    initialize() # doing initialize again to reset, so we're not locked out right now
    print(login("guerzhoy", "pythonismeh"))
    print(login("guerzhoy", "pythonismeh"))
    print(login("stangeby", "rigorous"))
    print(login("guerzhoy", "pythonismeh"))
    print(login("stangeby", "rigorous"))
    # still true! since after getting third login correct, the incorrect logins reset
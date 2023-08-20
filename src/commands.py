from testDBconnection import testdbconn


def commands(choice):
    if choice == "-tc":
        testdbconn()
    elif choice == "-v":
        print("Version #1.0")
    elif choice == "exit":
        exit(0)
    else:
        print("[Error] No command")

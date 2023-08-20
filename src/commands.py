from testDBconnection import testdbconn
from init import initialization
from pars import pars


def commands(choice):
    if choice == "-tc":
        testdbconn()
    elif choice == "-v":
        print("Version #1.0")
    elif choice == "-init":
        initialization()
    elif choice == "-p":
        pars()
    elif choice == "exit":
        exit(0)
    else:
        print("[Error] No command")

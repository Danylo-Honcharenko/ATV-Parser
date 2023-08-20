import os
from pathlib import Path
import time


def initialization():
    if Path("set").is_dir():
        print("[Info] 'set' folder exist")
    else:
        os.mkdir("set")

    if os.path.isfile("./set/atvList.txt"):
        print("[Info] File 'atvList.txt' already exists")
    else:
        with open("./set/atvList.txt", "w") as file:
            file.write("# Parser control file")
        file.close()

        print("Created 'atvList.txt'...")
        time.sleep(3)

        print("\nInitialization successful!")

from pathlib import Path
from commands import commands
import time
import os
from testDBconnection import testdbconn

if Path("./set/atv.conf").is_file():
    while True:
        choice = input("[atvp]> ")
        commands(choice)
else:
    print("Welcome! Let's create a configuration file")
    print("[Info] Configuration file can be created by yourself\n")

    dbHost = input("Database host: ")
    dbPort = input("Database port: ")
    dbUser = input("Database user: ")
    dbUserPass = input("Database user password: ")
    dbName = input("Database name: ")

    if Path("set").is_dir():
        print("\n[Info] 'set' folder exist")
    else:
        os.mkdir("set")

    with open("./set/atv.conf", "w") as file:
        file.write(f"[DBSETTINGS]\n")
        file.write(f"host = {dbHost}\n")
        file.write(f"port = {dbPort}\n")
        file.write(f"user = {dbUser}\n")
        file.write(f"database_user_password = {dbUserPass}\n")
        file.write(f"database_name = {dbName}")
    file.close()

    print("[Info] All data is saved in the 'atv.conf' file!\n")
    print("Now we are testing the database connection!")
    print("[Info] If you get an error then edit the configuration file")

    time.sleep(8)
    testdbconn()
    time.sleep(4)

    os.system("cls")

    while True:
        choice = input("[atvp]> ")
        commands(choice)

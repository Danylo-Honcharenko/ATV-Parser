import os
from pathlib import Path
from choices import choices

if Path("./set/atv.conf").is_file():
    while True:
        choice = input("[atvp]> ")
        choices(choice)
else:
    print("Welcome! Let's create a configuration file")
    print("*Configuration file can be created by yourself\n")

    dbHost = input("Database host: ")
    dbPort = input("Database port: ")
    dbUser = input("Database user: ")
    dbUserPass = input("Database user password: ")
    dbName = input("Database name: ")

    if Path("set").is_dir():
        print("'set' folder exist")
    else:
        os.mkdir("set")

    with open("./set/atv.conf", "w") as file:
        file.write(f"# db settings")
        file.write(f"Host: {dbHost}\n")
        file.write(f"Port: {dbPort}\n")
        file.write(f"User: {dbUser}\n")
        file.write(f"Database user password: {dbUserPass}\n")
        file.write(f"Database name: {dbName}")
    file.close()

    print("All data is saved in the 'atv.conf' file!")

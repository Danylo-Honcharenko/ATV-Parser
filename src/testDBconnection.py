from configparser import ConfigParser
import mysql.connector


def testdbconn():
    config_object = ConfigParser()
    config_object.read("./set/atv.conf")

    DBSettings = config_object["DBSETTINGS"]
    dbhost = DBSettings["host"]
    dbport = DBSettings["port"]
    dbuser = DBSettings["user"]
    dbpass = DBSettings["database_user_password"]

    try:
        conn = mysql.connector.connect(user=dbuser, password=dbpass, host=dbhost, port=dbport)
        print("Happy Connect!")
        conn.close()
    except mysql.connector.Error as err:
        print("[Error] Connect to DB error. More: {}".format(err))

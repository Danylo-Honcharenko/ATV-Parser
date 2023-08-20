# How to work with config file?
After the first launch of the program, 
you are given the opportunity to enter 
all the information about the database. 
After successful entry, these data are stored 
in `/set/atv.conf` and will be used to connect 
to the database in the future.

**Note also that `/set/atv.conf` must be located in the `set` folder!**
If you want to create it yourself, then you must adhere 
to the following structure:

```
[DBSETTINGS]
host = 127.0.0.1
port = 3306
user = test
database_user_password = 123456789
database_name = test
```
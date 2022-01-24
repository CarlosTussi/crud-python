import mysql.connector
import dbconfig

mydb = mysql.connector.connect(
    host= dbconfig.host,
    user=dbconfig.user,
    password=dbconfig.password
)

print(mydb)
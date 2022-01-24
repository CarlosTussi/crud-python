import mysql.connector
import dbconfig

mydb = mysql.connector.connect(
    host= dbconfig.host,
    user=dbconfig.user,
    password=dbconfig.password,
    database=dbconfig.database
)

mycursor = mydb.cursor()

######################
###CREATING A DATABASE
######################
# mycursor.execute("CREATE DATABASE mydatabase")

###Showing the results
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

###################
###CREATING A TABLE
###################
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

###Showing the results
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)


# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

###################
###INSERTING A ROW
###################
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

###It's a must
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")


######################
###INSERTING MANY ROWS
######################

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val) 

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
# print("1 record inserted, ID:", mycursor.lastrowid)



#########
###SELECT
#########
# mycursor.execute("SELECT * FROM customers")
# mycursor.execute("SELECT address FROM customers")

###Fetches all rows from the last executed statement
# myresult = mycursor.fetchall()  
###Fetches only the fist row of the result
# myresult = mycursor.fetchone()  

# for x in myresult:
#     print(x)


########
###WHERE
########
# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

#############
###ORDERED BY
#############
# sql = "SELECT * FROM customers ORDER BY name"
# sql = "SELECT * FROM customers ORDER BY name DESC"

#########
###DELETE
#########
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

#############
###DROP TABLE
#############
# sql = "DROP TABLE customers"
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)


###############
###UPDATE TABLE
###############
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()


###################
###LIMIT THE RESULT
###################
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


#######
###JOIN
#######

# sql = "SELECT \
#     users.name AS user, \
#     products.name AS favorite \
#     FROM users \
#     JOIN products ON users.fav = products.id"

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
import mysql.connector
import dbconfig

mydb = mysql.connector.connect(
    host= dbconfig.host,
    user=dbconfig.user,
    password=dbconfig.password,
    database=dbconfig.database
)

mycursor = mydb.cursor()


# mycursor.execute("DROP TABLE IF EXISTS actor")
# mycursor.execute("DROP TABLE IF EXISTS customers")
# mycursor.execute("DROP DATABASE IF EXISTS mydatabase")

##Creates MOVIE DATABASE
mycursor.execute("CREATE DATABASE IF NOT EXISTS movie_db")


##Creates MOVIES table
mycursor.execute("CREATE TABLE IF NOT EXISTS movies \
                    (id INT AUTO_INCREMENT PRIMARY KEY,\
                    name VARCHAR(255), \
                    director VARCHAR(255), \
                    country VARCHAR(255), \
                    year YEAR(4), \
                    genre VARCHAR(255))") 

##Creates ACTOR table
mycursor.execute("CREATE TABLE IF NOT EXISTS actors \
                    (id INT AUTO_INCREMENT PRIMARY KEY,\
                    first_name VARCHAR(255), \
                    last_name VARCHAR(255), \
                    gender VARCHAR(255))") 



##Creates MOVIE_CAST table
mycursor.execute("CREATE TABLE IF NOT EXISTS movie_cast \
                    (movie_id INT(4), \
                     actor_id INT(4), \
                     role VARCHAR(255))")



##Populating MOVIES table
# sql = "INSERT INTO movies (name, director, country, year, genre) VALUES (%s, %s, %s, %s, %s)"
# value = [
#     ('Dont look up', 'Adam McKay', 'US', '2021', 'Comedy'),
#     ('Anna', 'Luc Besson', 'Russia', '2022', 'Action'),
#     ('Forgotten', 'Hanjg-jun Jang', 'South Korea', '2017', 'Thriller'),
#     ('The Hunger Games', 'Gary Ross','US' , '2012', 'Sci-fi')
# ]
# mycursor.executemany(sql, value)
# mydb.commit()

print('\n')
print("=-MOVIES-=")
mycursor.execute("SELECT * FROM movies")
for x in mycursor:
    print(x)
print('\n')

##Populating ACTORS table
# sql = "INSERT INTO actors (first_name, last_name, gender) VALUES (%s, %s, %s)"
# value = [
#     ('Jennifer', 'Lawrance', 'F'),
#     ('Sasha', 'Luss', 'F')
# ]

# mycursor.executemany(sql, value)
# mydb.commit()
print("=-ACTORS-=")
mycursor.execute("SELECT * FROM actors")
for x in mycursor:
    print(x)
print('\n')


##Populating MOVIE_CAST table
# sql = "INSERT INTO movie_cast (movie_id, actor_id, role) VALUES (%s, %s, %s)"
# value =[
#     ('1', '3', 'Kate Dibiansky'),
#     ('7', '3', 'Katniss Everdeen'),
#     ('2', '4', 'Anna')
# ]

# mycursor.executemany(sql, value)
# mydb.commit()

print("=-MOVIE_CAST-=")
mycursor.execute("SELECT * FROM movie_cast")
for x in mycursor:
    print(x)
print('\n')

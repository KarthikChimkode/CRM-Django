import MySQLdb

dataBase = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Udemy@123'
)


# Prepare a cursor object
cursorObject = dataBase.cursor()


# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE!")
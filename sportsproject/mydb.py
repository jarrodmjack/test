import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='sportsapp'
)

#prepare cursor object
cursor_object = database.cursor()


# Create database
cursor_object.execute("CREATE DATABASE sportsappdb")

print('All done!')
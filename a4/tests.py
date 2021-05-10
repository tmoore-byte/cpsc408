import tables
import mysql.connector

db = mysql.connector.connect(
    host="34.94.182.22",
    user="tmoore@chapman.edu",
    password="FooBar!@#$",
    database="tmoore_db"
)
mycursor = db.cursor()


# TEST FUNCTIONS
# showing all tables
def showT():
    mycursor.execute("show tables")
    x = mycursor.fetchall()
    print(x)

def showdb():
    mycursor.execute("show database")
    x = mycursor.fetchall()
    print(x)


# dropping tables
def drop():
    mycursor.execute("DROP TABLE IF EXISTS CarModels, Customers, Payments, Sales, Employees")
    y = mycursor.fetchall()
    print(y)

import mysql.connector
import tests
import csv
import random as rand
from faker import Faker

# establishing connection stream
db = mysql.connector.connect(
    host="34.94.182.22",
    user="tmoore@chapman.edu",
    password="FooBar!@#$",
    database="tmoore_db"
)
mycursor = db.cursor()

def create_tables():
    mycursor.execute("CREATE TABLE Customers (customerID INT AUTO_INCREMENT PRIMARY KEY, cName VARCHAR(50), email VARCHAR(50), address VARCHAR(100))")
    mycursor.execute("CREATE TABLE Payments (customerID INT AUTO_INCREMENT PRIMARY KEY, paymentAmount INT UNSIGNED, paymentDate DATE)")
    # mycursor.execute("CREATE TABLE CarModels (modelCodeC INT AUTO_INCREMENT PRIMARY KEY, seriesNumber TINYINT UNSIGNED, numInStock SMALLINT UNSIGNED, listPrice INT UNSIGNED)")
    mycursor.execute("CREATE TABLE Sales(orderNumber INT NOT NULL, modelCode INT NOT NULL, salePrice INT UNSIGNED, saleDate DATE, saleStatus VARCHAR(20))")
    mycursor.execute("CREATE TABLE Employees (employeeID INT AUTO_INCREMENT PRIMARY KEY , eName VARCHAR(50), jobTitle VARCHAR(50), salary INT UNSIGNED)")

    print("showing tables")
    tests.showT()

def fakeData(fileName, numRecords):
    # opening  file
    f = open(fileName, "w")
    # writing to specified file
    w = csv.writer(f)

    w.writerow(["orderNumber", "seriesNumber", "saleStatus", "customerID", "modelCodeC", "modelCode", "numInStock", "listPrice", "paymentAmount", "paymentDate", "salePrice", "saleDate", "cName", "email", "address", "employeeID", "eName", "jobTitle", "salary"])
    # lists for indexing
    jobTitles = ["Sales", "Office", "Mechanic", "Boss", "Other"]
    sales = ["Pending", "Complete", "Received"]

    # for grabbing a random index of the lists we made above
    rJob = rand.randint(0, 4)
    rSales = rand.randint(0, 2)

    for i in range(0, numRecords):
        # using faker to generate data
        fake = Faker()
        w.writerow([
        fake.random_int(0, 2000),  # orderNumber
        fake.random_int(1, 6),  # seriesNumber
        sales[rSales],  # saleStatus
        fake.random_int(1, 2000),  # customerID
        fake.random_int(100, 800),  # modelCodeC
        fake.random_int(100, 800),  # modelCode
        fake.random_int(0, 100),  # numInStock
        fake.random_int(9000, 250000),  # listPrice
        fake.random_int(5000, 200000),  # paymentAmount
        fake.date(),  # paymentDate
        fake.random_int(9000, 300000),  # salePrice
        fake.date(),  # saleDate
        fake.name(),  # cName
        fake.email(),  # email
        fake.address(),  # address
        fake.random_int(1, 100),  # employeeID
        fake.name(),  # eName
        jobTitles[rJob],  # jobTitle
        fake.random_int(10000, 200000)])  # salary

    return fileName

def fill_data(fileName):
    mycursor = db.cursor()
    with open(fileName) as file1:
        reader = csv.DictReader(file1)
        for r in reader:  # iterate through each row
            mycursor.execute("INSERT INTO Customers(customerID, cName, email, address) VALUES(%s,%s,%s,%s);", (r["customerID"], r["cName"], r["email"], r["address"]))
            db.commit()

            mycursor.execute("INSERT INTO Payments(customerID, paymentAmount, paymentDate) VALUES(%s,%s,%s);", (r["customerID"], r["paymentAmount"], r["paymentDate"]))
            db.commit()

            mycursor.execute("INSERT INTO CarModels(modelCodeC, seriesNumber, numInStock, listPrice) VALUES(%s,%s,%s,%s);", (r["modelCodeC"], r["seriesNumber"], r["numInStock"], r["listPrice"]))
            db.commit()

            mycursor.execute("INSERT INTO Sales(orderNumber, modelCode, salePrice, saleDate, saleStatus) VALUES(%s,%s,%s,%s,%s);", (r["orderNumber"], r["modelCode"], r["salePrice"], r["saleDate"], r["saleStatus"]))
            db.commit()

            mycursor.execute("INSERT INTO Employees(employeeID, eName, jobTitle, salary) VALUES(%s,%s,%s,%s);", (r["employeeID"], r["eName"], r["jobTitle"], r["salary"]))
            db.commit()

            print("Imported: ", r)

















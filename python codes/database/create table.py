import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test1",
  password="4Mu99BhzK8dr4vF1",
  database="login_database"
) 

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
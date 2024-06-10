import mysql.connector

# Database connection details (replace with your actual credentials)
host = "localhost"
user = "root"
password = "root"
database = "dbms_project"

try:
  connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
  print("Connection to MySQL database successful!")

except mysql.connector.Error as err:
  print(f"Error connecting to MySQL database: {err}")

finally:
  if connection:
    connection.close()
    print("Connection closed.")

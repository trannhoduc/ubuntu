import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='nhosql',
                             user='root',
                             password='22trannho')
   sql_select_Query = "SELECT * FROM test WHERE ID=2"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
  
   print ("Printing each row's column values i.e.  developer record")
   for row in records:
       print("Id = ", row[0], )
       print("Name = ", row[1])
       print("MSSV  = ", row[2], "\n")
   cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection.is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")
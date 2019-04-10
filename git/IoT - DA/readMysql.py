import mysql.connector
from mysql.connector import Error
try:
	mySQLconnection = mysql.connector.connect(host='localhost',
                             database='testdb',
                             user='usernho',
                             password='nho123')
	sql_select_Query = "select *from Cars ORDER BY id DESC LIMIT 1"
	cursor = mySQLconnection .cursor()
	cursor.execute(sql_select_Query)
	records = cursor.fetchall()
	print("Total number of rows: ", cursor.rowcount)

	for row in records:
		print("Id = ", row[0], )
		print("Name = ", row[1])
		print("Salary  = ", row[2], "\n")
	cursor.close()
   
except Error as e :
	print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
	if(mySQLconnection .is_connected()):
		mySQLconnection.close()
		print("MySQL connection is closed")
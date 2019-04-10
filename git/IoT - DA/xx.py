import mysql.connector
from mysql.connector import errorcode
def getDeveloperDetails(ID):
    try:
        mySQLConnection = mysql.connector.connect(host='localhost',
                                             database='testdb',
                                             user='usernho',
                                             password='nho123')
        cursor = mySQLConnection.cursor(prepared=True)
        sql_select_query = """select * from Cars where id = %s"""
        cursor.execute(sql_select_query, (ID, ))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Salary  = ", row[2], "\n")
    except mysql.connector.Error as error:
        print("Failed to get record from database: {}".format(error))
    finally:
        # closing database connection.
        if (mySQLConnection.is_connected()):
            cursor.close()
            mySQLConnection.close()
            print("connection is closed")
id1 = 1
id2 = 2
getDeveloperDetails(id1)
getDeveloperDetails(cursor.rowcount)
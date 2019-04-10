
from guizero import *
import random
import mysql.connector
from mysql.connector import Error


def read():
    mySQLconnection = mysql.connector.connect(host='localhost',
                            database='testdb',
                            user='usernho',
                            password='nho123')
    sql_select_Query = "select *from rpi ORDER BY id DESC LIMIT 1"
    cursor = mySQLconnection .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
    #   print("Id = ", row[0], )
    #   print("Name = ", row[1])
    #   print("Salary  = ", row[2], "\n")
      a = row[2]
    return a

def readd():
    mySQLconnection = mysql.connector.connect(host='localhost',
                            database='testdb',
                            user='usernho',
                            password='nho123')
    sql_select_Query = "select *from rpi ORDER BY id DESC LIMIT 1"
    cursor = mySQLconnection .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
    #   print("Id = ", row[0], )
    #   print("Name = ", row[1])
    #   print("Salary  = ", row[2], "\n")
      a = row[1]
    return a    


def update_label():
    text.set(read())
    textt.set(readd())
    # recursive call
    text.after(2000, update_label)


if __name__ == '__main__':
    app = App(title='Sensor Display!',
              height=100,
              width=200,
              layout='grid')

    title = Text(app, 'Temperature:', grid=[0, 0])
    text = Text(app, "Temp", grid=[1, 0])
    titlee = Text(app, 'Humidity:', grid=[0, 1])
    textt = Text(app, "Humd", grid=[1, 1])


    text.after(2000, update_label)
    app.display()
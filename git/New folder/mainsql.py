
from PyQt5 import QtCore, QtGui, QtWidgets
from random import seed, randint
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from gui import Ui_DataDisplay  # importing our generated file

import mysql.connector
from mysql.connector import Error

import sys

seed(1)
 


class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_DataDisplay()
		self.ui.setupUi(self)

	def update_label(self):
		update = randint(0, 10)
		self.ui.textBrowser.setText(str(update))
		mySQLconnection = mysql.connector.connect(host='localhost',
                             database='nhosql',
                             user='root',
                             password='22trannho')
		sql_select_Query = "SELECT * FROM test WHERE ID=2"
		cursor = mySQLconnection .cursor()
		cursor.execute(sql_select_Query)
		records = cursor.fetchall()
		for row in records:
			self.ui.textBrowser_2.setText(row[1])		
		# self.update = update.label_update(self)

 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
timer = QTimer()
timer.timeout.connect(application.update_label)
timer.start(2000)
sys.exit(app.exec())
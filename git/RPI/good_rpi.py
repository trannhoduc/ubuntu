
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from good import Ui_DataDisplay  # importing our generated file

import mysql.connector
from mysql.connector import Error

import sys

 
class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_DataDisplay()
		self.ui.setupUi(self)
		self.setWindowIcon(QIcon("bk.ico"))

	def update_label(self):
		mySQLconnection = mysql.connector.connect(host='localhost',
                             database='sls_db',
                             user='root',
                             password='Son100480')
		sql_select_Query = "SELECT * FROM sls_db WHERE ID=2"
		cursor = mySQLconnection .cursor()
		cursor.execute(sql_select_Query)
		records = cursor.fetchall()
		for row in records:
			self.ui.textBrowser_2.setText(str(row[28]))	
			self.ui.textBrowser.setText(str(row[27]))
			self.ui.textBrowser_3.setText(str(row[26]))
			self.ui.textBrowser_4.setText(str(row[29]))	
		# self.update = update.label_update(self)

 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
timer = QTimer()
timer.timeout.connect(application.update_label)
timer.start(2000)
sys.exit(app.exec())
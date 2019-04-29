
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_DataDisplay  # importing our generated file
import sys
 
class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_DataDisplay()
		self.ui.setupUi(self)

def start_timer(slot, count=1, interval=1000):
	counter = 0
	def handler():
		nonlocal counter
		counter += 1
		slot(counter)
		if counter >= count:
			timer.stop()
			timer.deleteLater()
	timer = QtCore.QTimer()
	timer.timeout.connect(handler)
	timer.start(interval)

def changeText(count):
	self.ui.label.setText("hola")
	if count >= 3:
		QtCore.QCoreApplication.quit()
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
start_timer(changeText, 3)
sys.exit(app.exec())
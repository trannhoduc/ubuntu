# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'good.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataDisplay(object):
    def setupUi(self, DataDisplay):
        DataDisplay.setObjectName("DataDisplay")
        DataDisplay.resize(480, 300)
        self.centralwidget = QtWidgets.QWidget(DataDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("SFU TheSans")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("SFU TheSans")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 110, 181, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(270, 180, 181, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(-200, 590, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("50.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("UTM Bebas")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("UTM Bebas")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 110, 181, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(30, 180, 181, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("SFU TheSans")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("SFU TheSans")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 230, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 230, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        DataDisplay.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataDisplay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        self.menuNN = QtWidgets.QMenu(self.menubar)
        self.menuNN.setObjectName("menuNN")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        DataDisplay.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataDisplay)
        self.statusbar.setObjectName("statusbar")
        DataDisplay.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(DataDisplay)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(DataDisplay)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(DataDisplay)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(DataDisplay)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(DataDisplay)
        self.actionPaste.setObjectName("actionPaste")
        self.menuNN.addAction(self.actionNew)
        self.menuNN.addAction(self.actionOpen)
        self.menuNN.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuNN.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(DataDisplay)
        QtCore.QMetaObject.connectSlotsByName(DataDisplay)

    def retranslateUi(self, DataDisplay):
        _translate = QtCore.QCoreApplication.translate
        DataDisplay.setWindowTitle(_translate("DataDisplay", "Data display"))
        self.label.setText(_translate("DataDisplay", "Light"))
        self.label_2.setText(_translate("DataDisplay", "Pressure"))
        self.label_5.setText(_translate("DataDisplay", "<html><head/><body><p><span style=\" color:#0055ff;\">TRƯỜNG ĐẠI HỌC BÁCH KHOA</span></p></body></html>"))
        self.label_6.setText(_translate("DataDisplay", "<html><head/><body><p><span style=\" color:#0055ff;\">ĐẠI HỌC QUỐC GIA TP.HCM</span></p></body></html>"))
        self.label_3.setText(_translate("DataDisplay", "Temperature"))
        self.label_7.setText(_translate("DataDisplay", "Humidity"))
        self.pushButton.setText(_translate("DataDisplay", "Stop"))
        self.pushButton_2.setText(_translate("DataDisplay", "MQTT"))
        self.menuNN.setTitle(_translate("DataDisplay", "File"))
        self.menuEdit.setTitle(_translate("DataDisplay", "Edit"))
        self.menuSettings.setTitle(_translate("DataDisplay", "Settings"))
        self.actionNew.setText(_translate("DataDisplay", "New"))
        self.actionOpen.setText(_translate("DataDisplay", "Open"))
        self.actionSave.setText(_translate("DataDisplay", "Save"))
        self.actionCopy.setText(_translate("DataDisplay", "Copy"))
        self.actionPaste.setText(_translate("DataDisplay", "Paste"))

# import py_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataDisplay = QtWidgets.QMainWindow()
    ui = Ui_DataDisplay()
    ui.setupUi(DataDisplay)
    DataDisplay.show()
    sys.exit(app.exec_())


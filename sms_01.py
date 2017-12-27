# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMS.ui'
#
# Created: Tue Aug 15 13:07:25 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from twilio.rest import Client

class MyApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        #self.send_Button.clicked.connect(self.send_Message)
        QtWidgets.QMainWindow.__init__(self)
        #Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.phone_number = QtWidgets.QTextEdit(self.centralwidget)
        self.phone_number.setGeometry(QtCore.QRect(280, 210, 271, 31))
        self.phone_number.setObjectName("phone_number")
        self.Phone_Number = QtWidgets.QLabel(self.centralwidget)
        self.Phone_Number.setGeometry(QtCore.QRect(140, 220, 111, 16))
        self.Phone_Number.setObjectName("Phone_Number")
        self.edit = QtWidgets.QLabel(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(150, 260, 91, 31))
        self.edit.setObjectName("edit")
        self.send_message = QtWidgets.QTextEdit(self.centralwidget)
        self.send_message.setGeometry(QtCore.QRect(280, 260, 411, 221))
        self.send_message.setObjectName("send_message")
        self.account_sid = QtWidgets.QComboBox(self.centralwidget)
        self.account_sid.setGeometry(QtCore.QRect(280, 130, 231, 22))
        self.account_sid.setObjectName("account_sid")
        self.account_sid.addItem("")
        self.account_sid.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 130, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 170, 61, 20))
        self.label_2.setObjectName("label_2")
        self.auth_token = QtWidgets.QComboBox(self.centralwidget)
        self.auth_token.setGeometry(QtCore.QRect(280, 170, 231, 22))
        self.auth_token.setObjectName("auth_token")
        self.auth_token.addItem("")
        self.auth_token.addItem("")
        self.send_Button = QtWidgets.QPushButton(self.centralwidget)
        self.send_Button.setGeometry(QtCore.QRect(610, 500, 81, 31))
        self.send_Button.setObjectName("send_Button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 141, 41))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.send_Button.clicked.connect(self.send_Message)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Phone_Number.setText(_translate("MainWindow", "请输入接收手机号："))
        self.edit.setText(_translate("MainWindow", "请编辑短信内容："))
        self.account_sid.setItemText(0, _translate("MainWindow", "AC379cd2e6115757ed31a66346164e340c"))
        self.account_sid.setItemText(1, _translate("MainWindow", "123"))
        self.label.setText(_translate("MainWindow", "account_sid"))
        self.label_2.setText(_translate("MainWindow", "auth_token"))
        self.auth_token.setItemText(0, _translate("MainWindow", "dd1cb947e42ff7c831267c2877de509a"))
        self.auth_token.setItemText(1, _translate("MainWindow", "123"))
        self.send_Button.setText(_translate("MainWindow", "发送"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">短信发送器</span></p></body></html>"))

    def send_Message(self):
        # Your Account SID from twilio.com/console
        account_sid = self.account_sid.currentText()
        # Your Auth Token from twilio.com/console
        auth_token  = self.auth_token.currentText()

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=(self.phone_number.toPlainText()),
            from_="+12402216920",
            body=(self.send_message.toPlainText()))
    

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())


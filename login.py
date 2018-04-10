# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from welcome import Ui_Dialog1
import sqlite3
class Ui_Dialog(object):
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()
    def loginCheck(self):
         username = self.uname_edit.text()
         password = self.pass_edit.text()

         connection = sqlite3.connect("login.db")
         result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ?  AND PASSWORD = ?",(username,password))
         if(len(result.fetchall()) > 0):
             print("User Found")
             self.openWindow()
         else:
             print("User Not Found")
         
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 336)
        Dialog.setStyleSheet("background-color:rgb(0, 170, 255)qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(180, 190, 75, 23))
        self.login_btn.setObjectName("login_btn")
        ####Button event####
        self.login_btn.clicked.connect(self.loginCheck)  
        self.uname_edit = QtWidgets.QLineEdit(Dialog)
        self.uname_edit.setGeometry(QtCore.QRect(210, 120, 113, 20))
        self.uname_edit.setObjectName("uname_edit")
        self.pass_edit = QtWidgets.QLineEdit(Dialog)
        self.pass_edit.setGeometry(QtCore.QRect(210, 150, 113, 20))
        self.pass_edit.setObjectName("pass_edit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 120, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "USERNAME"))
        self.label_2.setText(_translate("Dialog", "PASSWORD"))
        self.label_3.setText(_translate("Dialog", "LOGIN PAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


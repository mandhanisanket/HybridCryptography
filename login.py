# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from welcome1 import Ui_welcomed
import _mysql


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def openWindow(self):
        self.window = QtGui.QDialog()
        self.ui = Ui_welcomed()
        self.ui.setupUi(self.window)
        Login.hide()
        self.window.show()
        
    def loginCheck(self):
         username = self.uname_linedit.text()
         password = self.pass_edit.text()
	 connection = _mysql.connect('localhost', 'root', '1234', 'login')
         connection.query("SELECT * FROM USERS;")
         result=connection.use_result()
    	 #print(result.fetch_row())
    	 
         if(len(result.fetch_row()) > 0):
             print("User Found")
             self.openWindow()
         else:
             print("User Not Found")
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(476, 347)
        self.label = QtGui.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(110, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(110, 170, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.uname_linedit = QtGui.QLineEdit(Login)
        self.uname_linedit.setGeometry(QtCore.QRect(210, 130, 113, 20))
        self.uname_linedit.setObjectName(_fromUtf8("uname_linedit"))
        self.pass_edit = QtGui.QLineEdit(Login)
        self.pass_edit.setGeometry(QtCore.QRect(210, 170, 113, 20))
        self.pass_edit.setObjectName(_fromUtf8("pass_edit"))
        
        self.pass_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.login_btn = QtGui.QPushButton(Login)
        self.login_btn.setGeometry(QtCore.QRect(180, 210, 75, 23))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.login_btn.clicked.connect(self.loginCheck)
        self.label_3 = QtGui.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Dialog", None))
        self.label.setText(_translate("Login", "USERNAME", None))
        self.label_2.setText(_translate("Login", "PASSWORD", None))
        self.login_btn.setText(_translate("Login", "Login", None))
        self.label_3.setText(_translate("Login", "LOGIN PAGE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

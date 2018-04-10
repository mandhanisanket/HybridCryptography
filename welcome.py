# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from upload import Ui_Dialog2
from download import Ui_Dialog3

class Ui_Dialog1(object):
    def openWindow1(self):
        self.window1 = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.window1)
        Dialog1.hide()
        self.window1.show()

    def openWindow2(self):
        self.window2 = QtWidgets.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self.window2)
        Dialog1.hide()
        self.window2.show()
  
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 337)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openWindow1)
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openWindow2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Upload file "))
        self.pushButton_2.setText(_translate("Dialog", "Download file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 336)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.file_name = QtWidgets.QLineEdit(Dialog)
        self.file_name.setGeometry(QtCore.QRect(220, 100, 113, 20))
        self.file_name.setObjectName("file_name")
        self.select = QtWidgets.QPushButton(Dialog)
        self.select.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.select.setObjectName("select")

        self.select.clicked.connect(self.button_click)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def button_click(self):
        shost = self.file_name.text()
        print(shost)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select a File:"))
        self.pushButton_2.setText(_translate("Dialog", "Upload"))
        self.select.setText(_translate("Dialog", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())


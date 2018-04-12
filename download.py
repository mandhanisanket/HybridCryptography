from PyQt4 import QtCore, QtGui
from enter_key import Ui_Dialog4

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

class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(470, 344)
        self.download_edit = QtGui.QLineEdit(Dialog)
        self.download_edit.setGeometry(QtCore.QRect(200, 150, 113, 20))
        self.download_edit.setObjectName(_fromUtf8("download_edit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 160, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.down_select_btn = QtGui.QPushButton(Dialog)
        self.down_select_btn.setGeometry(QtCore.QRect(320, 150, 75, 23))
        self.down_select_btn.setObjectName(_fromUtf8("down_select_btn"))
        self.down_select_btn.clicked.connect(self.button_click)
        
        self.download_btn = QtGui.QPushButton(Dialog)
        self.download_btn.setGeometry(QtCore.QRect(200, 190, 75, 23))
        self.download_btn.setObjectName(_fromUtf8("download_btn"))
        self.download_btn.clicked.connect(self.openwindow)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def openwindow(self):
        self.window1 = QtGui.QDialog()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self.window1)
        self.window1.show()
        	
    def button_click(self):
        shost1 = self.download_edit.text()
        print(shost1)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Download File", None))
        self.label_2.setText(_translate("Dialog", "Type the name of file:", None))
        self.label.setText(_translate("Dialog", "Download File", None))
        self.down_select_btn.setText(_translate("Dialog", "Select", None))
        self.download_btn.setText(_translate("Dialog", "Download", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog3 = QtGui.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())

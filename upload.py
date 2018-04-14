from PyQt4 import QtCore, QtGui
from generateKeys import genkey
from encipher import encipher
from encipher import cleanUp

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

# Sender's private key:
priKey = "priKey.pem"
# Receiver's public key:
pubKey = "pubKey.pem"

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(473, 343)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 160, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.upload_edit = QtGui.QLineEdit(Dialog)
        self.upload_edit.setGeometry(QtCore.QRect(200, 150, 113, 20))
        self.upload_edit.setObjectName(_fromUtf8("upload_edit"))
        self.up_select_btn = QtGui.QPushButton(Dialog)
        self.up_select_btn.setGeometry(QtCore.QRect(320, 150, 75, 23))
        self.up_select_btn.setObjectName(_fromUtf8("up_select_btn"))
        self.up_select_btn.clicked.connect(self.button_click)

        self.upload_btn = QtGui.QPushButton(Dialog)
        self.upload_btn.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.upload_btn.setObjectName(_fromUtf8("upload_btn"))
        self.upload_btn.clicked.connect(self.button_click1)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def openwindow(self):
        self.window1 = QtGui.QDialog()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self.window1)
        self.window1.show()
        	
    def button_click(self):
        shost = self.upload_edit.text()
        genkey() 
        print(shost)
        
    def button_click1(self):
        shost = self.upload_edit.text()
        encipher(priKey, pubKey, shost, "abc")
        cleanUp(shost)
        print(shost)
        
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Upload File", None))
        self.label.setText(_translate("Dialog", "Upload File", None))
        self.label_2.setText(_translate("Dialog", "Type the name of file:", None))
        self.up_select_btn.setText(_translate("Dialog", "Select", None))
        self.upload_btn.setText(_translate("Dialog", "Upload", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())

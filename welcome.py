from PyQt4 import QtCore, QtGui
from upload1 import Ui_Dialog2
from download1 import Ui_Dialog3

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

class Ui_welcomed(object):
    def openWindow1(self):
        self.window1 = QtGui.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.window1)
        #welcomed.hide()
        self.window1.show()

    def openWindow2(self):
        self.window2 = QtGui.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self.window2)
        #welcomed.hide()
        self.window2.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(473, 348)
        self.upload_btn = QtGui.QPushButton(Dialog)
        self.upload_btn.setGeometry(QtCore.QRect(175, 120, 110, 23))
        self.upload_btn.setObjectName(_fromUtf8("upload_btn"))
        self.upload_btn.clicked.connect(self.openWindow1)
        
        self.download_btn = QtGui.QPushButton(Dialog)
        self.download_btn.setGeometry(QtCore.QRect(175, 170, 110, 23))
        self.download_btn.setObjectName(_fromUtf8("download_btn"))
        self.download_btn.clicked.connect(self.openWindow2)
        
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Choose a task", None))
        self.upload_btn.setText(_translate("Dialog", "Upload File", None))
        self.download_btn.setText(_translate("Dialog", "Download File", None))
        self.label.setText(_translate("Dialog", "Choose a task ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    welcomed = QtGui.QDialog()
    ui = Ui_welcomed()
    ui.setupUi(welcomed)
    welcomed.show()
    sys.exit(app.exec_())

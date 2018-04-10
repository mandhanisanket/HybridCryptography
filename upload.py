import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    b1 = QtWidgets.QPushButton(w)
    l1 = QtWidgets.QLabel(w)
    l1.setText('Select File to Upload:')
    b.setText('Select')
    b1.setText('Upload')
    w.setWindowTitle('Upload')
    w.setGeometry(500, 250, 400, 300)
    l1.move(100, 100)
    b.move(220, 100)
    b1.move(150, 150)
    w.show()
    sys.exit(app.exec_())

window()

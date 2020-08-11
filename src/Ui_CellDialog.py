# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CellID.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QDialog, QApplication


class Ui_CellDialog(QDialog):
    def __init__(self):
        super(Ui_CellDialog, self).__init__()
        self.setupUi(self)
        # self.init(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 135)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 301, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 151, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search by cell ID or cell name"))
        self.label.setText(_translate("Dialog", "Select a cell ID or name you want to watch."))

    @staticmethod
    def getResult(cells):
        dialog = Ui_CellDialog()
        dialog.comboBox.clear()
        print(cells)
        dialog.comboBox.addItems(cells)
        result = dialog.exec_()
        selected = ''
        if result:
            selected = dialog.comboBox.currentText()
        return result, selected

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = Ui_CellDialog()

    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DateTimeSelect.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QDialog, QApplication


class Ui_DateTimeSelectDialog(QDialog):
    def __init__(self):
        super(Ui_DateTimeSelectDialog, self).__init__()
        self.setupUi(self)
        self.init(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 124)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 30, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(30, 80, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 141, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Time select"))
        self.label.setText(_translate("Dialog", "Select a start time"))
        self.label_2.setText(_translate("Dialog", "Select a end time"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))

    def init(self, Dialog):
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.pushButton.clicked.connect(Dialog.accept)
        self.pushButton_2.clicked.connect(Dialog.reject)

    def onPrint(self):
        print(self.dateTimeEdit.text())

    @staticmethod
    def getResult():
        dialog = Ui_DateTimeSelectDialog()
        result = dialog.exec_()
        time_from = dialog.dateTimeEdit.text()
        time_to = dialog.dateTimeEdit_2.text()
        if result:
            if time_from < time_to:
                return result, time_from, time_to


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = Ui_DateTimeSelectDialog()

    MainWindow.show()
    sys.exit(app.exec_())
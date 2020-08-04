# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, qApp, QFileDialog

from src.LogicCore import LogicCore
from src.Ui_RegisterDialog import Ui_RegisterDialog
from src.Ui_SignInDialog import Ui_SignInDialog
from src.Ui_LogOutDialog import Ui_LogOutDialog


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.init()
        self.retranslateUi(self)

        self.operations = LogicCore(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 110, 401, 241))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(140, 90, 54, 12))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 54, 12))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 54, 12))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSign_in = QtWidgets.QAction(MainWindow)
        self.actionSign_in.setObjectName("actionSign_in")
        self.actionLog_out = QtWidgets.QAction(MainWindow)
        self.actionLog_out.setObjectName("actionLog_out")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionAnalyse = QtWidgets.QAction(MainWindow)
        self.actionAnalyse.setObjectName("actionAnalyse")
        self.menuFile.addAction(self.actionSign_in)
        self.menuFile.addAction(self.actionLog_out)
        self.menuFile.addAction(self.actionRegister)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionSearch)
        self.menuTools.addAction(self.actionAnalyse)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def init(self):
        self.menubar.setNativeMenuBar(False)

        # Menu binding
        self.actionExit.triggered.connect(self.onExit)
        self.actionSign_in.triggered.connect(self.onSignIn)
        self.actionLog_out.triggered.connect(self.onLogOut)
        self.actionRegister.triggered.connect(self.onRegister)
        self.actionImport.triggered.connect(self.onImport)
        self.actionExport.triggered.connect(self.onExport)

        # Visual elements
        self.actionLog_out.setEnabled(False)

    def onSignIn(self):
        ok, info, account, password = Ui_SignInDialog.getResult(self)
        if ok:
            if self.operations.signIn(account, password):
                self.actionLog_out.setEnabled(True)
                self.actionSign_in.setEnabled(False)
                self.showStatus("Sign in successfully.")

    def onLogOut(self):
        ok = Ui_LogOutDialog.getResult()
        if ok:
            self.operations.logOut()
            self.showStatus("Logged out.")
            self.actionLog_out.setEnabled(False)
            self.actionSign_in.setEnabled(True)

    def onRegister(self):
        ok, info, account, pwd, pwd2 = Ui_RegisterDialog.getResult()
        if ok and pwd == pwd2:
            self.operations.register(account, pwd)
        elif pwd != pwd2:
            self.showStatus("The passwords do not match, try again.")

    def onImport(self):
        filenames = QFileDialog.getOpenFileNames(self,
                                                 'Choose files',
                                                 '/',
                                                 'Data files(*.xlsx , *.xls , *.csv)')

    def onExport(self):
        filenames = QFileDialog.getSaveFileName(self,
                                                'Save as',
                                                '/untitled',
                                                'Excel files(*.xlsx , *.xls)')

    def onExit(self):
        qApp.quit()

    def showStatus(self, msg):
        if msg:
            self.statusBar().showMessage(msg)
        else:
            self.statusBar().showMessage('ERR')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "pg1"))
        self.label_2.setText(_translate("MainWindow", "pg2"))
        self.label_3.setText(_translate("MainWindow", "pg3"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionSign_in.setText(_translate("MainWindow", "Sign in"))
        self.actionLog_out.setText(_translate("MainWindow", "Log out"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))
        self.actionImport.setText(_translate("MainWindow", "Import..."))
        self.actionExport.setText(_translate("MainWindow", "Export..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionAnalyse.setText(_translate("MainWindow", "Analyse"))

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()

    MainWindow.show()
    sys.exit(app.exec_())
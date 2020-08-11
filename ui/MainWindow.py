# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSearch = QtWidgets.QMenu(self.menuTools)
        self.menuSearch.setObjectName("menuSearch")
        self.menuAnalyse = QtWidgets.QMenu(self.menuTools)
        self.menuAnalyse.setObjectName("menuAnalyse")
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
        self.actionBy_cell_name_ID = QtWidgets.QAction(MainWindow)
        self.actionBy_cell_name_ID.setObjectName("actionBy_cell_name_ID")
        self.actionBy_eNodeB_name_ID = QtWidgets.QAction(MainWindow)
        self.actionBy_eNodeB_name_ID.setObjectName("actionBy_eNodeB_name_ID")
        self.actionKPI_indicator_diagram = QtWidgets.QAction(MainWindow)
        self.actionKPI_indicator_diagram.setObjectName("actionKPI_indicator_diagram")
        self.actionPRB_information_diagram = QtWidgets.QAction(MainWindow)
        self.actionPRB_information_diagram.setObjectName("actionPRB_information_diagram")
        self.menuFile.addAction(self.actionSign_in)
        self.menuFile.addAction(self.actionLog_out)
        self.menuFile.addAction(self.actionRegister)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSearch.addAction(self.actionBy_cell_name_ID)
        self.menuSearch.addAction(self.actionBy_eNodeB_name_ID)
        self.menuAnalyse.addAction(self.actionKPI_indicator_diagram)
        self.menuAnalyse.addAction(self.actionPRB_information_diagram)
        self.menuTools.addAction(self.menuSearch.menuAction())
        self.menuTools.addAction(self.menuAnalyse.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSearch.setTitle(_translate("MainWindow", "Search"))
        self.menuAnalyse.setTitle(_translate("MainWindow", "Analyse"))
        self.actionSign_in.setText(_translate("MainWindow", "Sign in"))
        self.actionLog_out.setText(_translate("MainWindow", "Log out"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))
        self.actionImport.setText(_translate("MainWindow", "Import..."))
        self.actionExport.setText(_translate("MainWindow", "Export..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionBy_cell_name_ID.setText(_translate("MainWindow", "By cell name/ID"))
        self.actionBy_eNodeB_name_ID.setText(_translate("MainWindow", "By eNodeB name/ID"))
        self.actionKPI_indicator_diagram.setText(_translate("MainWindow", "KPI indicator diagram"))
        self.actionPRB_information_diagram.setText(_translate("MainWindow", "PRB information diagram"))

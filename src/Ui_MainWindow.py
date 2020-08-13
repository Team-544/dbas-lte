# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, qApp, QFileDialog

from src.LogicCore import LogicCore
from src.Ui_C2IDialog import Ui_C2IDialog
from src.Ui_CellDialog import Ui_CellDialog
from src.Ui_ENodeBDialog import Ui_ENodeBDialog
from src.Ui_ExportDialog import Ui_ExportDialog
from src.Ui_ImportDialog import Ui_ImportDialog
from src.Ui_KPIDialog import Ui_KPIDialog
from src.Ui_PRBDialog import Ui_PRBDialog
from src.Ui_ParameterSettingDialog import Ui_ParameterSettingDialog
from src.Ui_RegisterDialog import Ui_RegisterDialog
from src.Ui_ResultDialog import Ui_ResultDialog
from src.Ui_SignInDialog import Ui_SignInDialog
from src.Ui_LogOutDialog import Ui_LogOutDialog
from src.Visualization import Visualization

LOG_IN_CONFIRM = False

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.init()

        self.operations = LogicCore(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 200, 281, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 22))
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
        self.actionLog_out.setEnabled(False)
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
        self.actionC2I_Analyse = QtWidgets.QAction(MainWindow)
        self.actionC2I_Analyse.setObjectName("actionC2I_Analyse")
        self.actionOverlapping_interference_triples = QtWidgets.QAction(MainWindow)
        self.actionOverlapping_interference_triples.setObjectName("actionOverlapping_interference_triples")
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
        self.menuSearch.addAction(self.actionOverlapping_interference_triples)
        self.menuAnalyse.addAction(self.actionKPI_indicator_diagram)
        self.menuAnalyse.addAction(self.actionPRB_information_diagram)
        self.menuAnalyse.addAction(self.actionC2I_Analyse)
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
        self.actionC2I_Analyse.setText(_translate("MainWindow", "C2I Analyse"))
        self.actionOverlapping_interference_triples.setText(_translate("MainWindow", "Overlapping interference triples"))

    def init(self):
        self.menubar.setNativeMenuBar(False)

        # Menu binding
        self.actionExit.triggered.connect(self.onExit)
        self.actionSign_in.triggered.connect(self.onSignIn)
        self.actionLog_out.triggered.connect(self.onLogOut)
        self.actionRegister.triggered.connect(self.onRegister)
        self.actionImport.triggered.connect(self.onImport)
        self.actionExport.triggered.connect(self.onExport)
        self.actionBy_cell_name_ID.triggered.connect(self.onSearchCell)
        self.actionBy_eNodeB_name_ID.triggered.connect(self.onSearchENodeB)
        self.actionKPI_indicator_diagram.triggered.connect(self.onKPI)
        self.actionPRB_information_diagram.triggered.connect(self.onPRB)
        self.actionC2I_Analyse.triggered.connect(self.onC2IAnalyse)
        self.actionOverlapping_interference_triples.triggered.connect(self.onTriples)

        # Visual elements
        if LOG_IN_CONFIRM:
            self.actionLog_out.setEnabled(False)
            self.menuTools.setEnabled(False)
            self.actionExport.setEnabled(False)
            self.actionImport.setEnabled(False)

        # test

    def onSignIn(self):
        ok, info, account, password = Ui_SignInDialog.getResult(self)
        if ok:
            if self.operations.signIn(account, password):
                if LOG_IN_CONFIRM:
                    self.actionLog_out.setEnabled(True)
                    self.actionSign_in.setEnabled(False)
                    self.menuTools.setEnabled(True)
                    self.actionExport.setEnabled(True)
                    self.actionImport.setEnabled(True)
                    self.label.setText('Log in as:')
                    self.label_2.setText('Log in time:')
                    self.label_3.setText(account)
                    self.label_4.setText(str(time.asctime(time.localtime(time.time()))))
                self.showStatus("Sign in successfully.")

    def onLogOut(self):
        ok = Ui_LogOutDialog.getResult()
        if ok:
            self.operations.logOut()
            self.showStatus("Logged out.")
            if LOG_IN_CONFIRM:
                self.actionLog_out.setEnabled(False)
                self.actionSign_in.setEnabled(True)
                self.menuTools.setEnabled(False)
                self.actionExport.setEnabled(False)
                self.actionImport.setEnabled(False)
                self.label.clear()
                self.label_2.clear()
                self.label_3.clear()
                self.label_4.clear()

    def onRegister(self):
        ok, info, account, pwd, pwd2 = Ui_RegisterDialog.getResult()
        if ok and pwd == pwd2:
            self.operations.register(account, pwd)
        elif pwd != pwd2:
            self.showStatus("The passwords do not match, try again.")

    def onImport(self):
        ok = Ui_ImportDialog.getResult(self.operations.db.getTables(), self.operations.myImport)
        if ok:
            self.showStatus('Import successfully')

    def onExport(self):
        ok, table, filename = Ui_ExportDialog.getResult(self.operations.db.getTables())
        if ok:
            self.operations.data_export(filename, table)
            self.showStatus('Export successfully')

    def onExit(self):
        qApp.quit()

    def onKPI(self):
        attrs = self.operations.db.getTbCols('tbKPI')
        NE_names = self.operations.db.getNENames('tbKPI')

        # ok, start_time, end_time, ne, attr = Ui_KPIDialog.getResult(attrs, NE_names)
        # if ok:
        #     date, attributes = self.operations.search_KPI(ne, start_time, end_time, attr)
        attr=''
        Visualization.showPlot(['2016-07-17 00:00:00', '2016-07-18 00:00:00', '2016-07-19 00:00:00'], [0.001, 0.002, 0.004], 'Time', attr, attr + '-Time Diagram')
        # else:
        #     self.showStatus('Some thing wrong.')

    def onPRB(self):
        attrs = self.operations.db.getTbCols('tbPRB')
        NE_names = self.operations.db.getNENames('tbPRB')
        ok, start_time, end_time, ne, attr = Ui_PRBDialog.getResult(attrs, NE_names)
        if ok:
            date, attributes = self.operations.search_PRB(ne, start_time, end_time, attr)
            Visualization.showPlot(['2016-07-17 00:00:00', '2016-07-18 00:00:00', '2016-07-19 00:00:00'], [0.001, 0.002, 0.004], 'Time', attr, attr + '-Time Diagram')
        else:
            self.showStatus('Some thing wrong.')

    def onAnalyse(self):
        # for test
        ok = Ui_ResultDialog.getResult(['1', '2', '3'], [('abc', 'def', 'ghi'), ('abc', 'def', 'ghi')])

    def onSearchCell(self):
        ok, cell = Ui_CellDialog.getResult(self.operations.db.getCells())
        lines = self.operations.search_tbCell(cell)
        if ok:
            cols = self.operations.db.getTbCols('tbCell')
            ok = Ui_ResultDialog.getResult(cols, lines)

    def onSearchENodeB(self):
        ok, eNodeB = Ui_ENodeBDialog.getResult(self.operations.db.getENodeBs())
        lines = self.operations.search_eNodeB(eNodeB)
        if ok:
            cols = self.operations.db.getTbCols('tbCell')
            ok = Ui_ResultDialog.getResult(cols, lines)

    def onC2IAnalyse(self):
        ok, ratio = Ui_ParameterSettingDialog.getResult('Please appoint a filtrate value:', 100, '')
        if ok:
            self.operations.create_C2I_table(ratio)
            Ui_C2IDialog.getResult(self.operations,
                                   self.operations.db.getCellInC2I('SCELL'),
                                   self.operations.db.getCellInC2I('NCELL'))

    def onTriples(self):
        ok, ratio = Ui_ParameterSettingDialog.getResult('Please appoint a filtrate value:', 100, '')
        if ok:
            self.operations.create_C2I_table(ratio)
            print('table created')
            ok, ratio = Ui_ParameterSettingDialog.getResult('Set a PrbABS6 ratio', 100, '%')
            if ok:
                print(ratio)
                result = self.operations.trigroup_search(ratio)
                print('ready to show')
                Ui_ResultDialog.getResult(['CELL1', 'CELL2', 'CELL3'], result)

    def showStatus(self, msg):
        if msg:
            self.statusBar().showMessage(msg)
        else:
            self.statusBar().showMessage('ERR')


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()

    MainWindow.show()
    sys.exit(app.exec_())

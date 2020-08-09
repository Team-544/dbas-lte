import sys
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

#demo_5:重新关闭按钮x关闭事件，给个提示框提示
class Exception(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('添加关闭按钮')
        self.setFont(QFont('微软雅黑',20))
        self.resize(400,300)
        self.setWindowIcon(QIcon('1.png'))

        #居中窗口
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.show()

    def closeEvent(self, QCloseEvent):
        res=QMessageBox.question(self,'消息','是否关闭这个窗口？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No) #两个按钮是否， 默认No则关闭这个提示框
        if res==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



if __name__=='__main__':
    # pp=QApplication(sys.argv)
    # example=Exception()
    # #example.show()
    # sys.exit(pp.exec())

    a = [1, 3, 4, 4]
    print(len(a))
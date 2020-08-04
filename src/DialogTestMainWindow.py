import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from src.SignInDialog import Ui_SignInDialog


class Win(QWidget):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.resize(400, 400)

        self.btn = QPushButton("按钮", self)
        self.btn.move(50, 50)
        self.btn.setMinimumWidth(80)

        # 显示子窗口传来的日期字符串或者其他数据
        self.label = QLabel('显示信息', self)
        self.label.setMinimumWidth(420)

        self.btn.clicked.connect(self.fn)

    def fn(self):
        account, password, res = Ui_SignInDialog.getResult(self)
        print(account, password, res)


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())

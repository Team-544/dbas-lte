import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from src.Ui_MainWindow import Ui_MainWindow

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
print()
    MainWindow.show()
    sys.exit(app.exec_())
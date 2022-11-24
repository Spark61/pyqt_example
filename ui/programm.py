import sys

from PyQt5.QtWidgets import QMainWindow,QApplication
import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("hauptprogramm.ui")
        self.show()


app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('ui/maler.ui', self)  # Load the .ui file






app = QApplication([])
w = MainWindow()
w.show()
app.exec()
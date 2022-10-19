from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("MiniProg")
        self.setWindowIcon(QIcon("sample.png"))
        self.statusBar().showMessage("Information zum Programm")


app = QApplication([])
w = Fenster()
w.show()
app.exec()

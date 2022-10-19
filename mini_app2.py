from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QStatusBar


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("MiniProg")
        self.setWindowIcon(QIcon("sample.png"))

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        exitMe = QAction(QIcon("sample.png"), "&Exit1", self)
        exitMe.setShortcut("Ctrl+Q")
        exitMe.setStatusTip("Unser Exit")
        exitMe.triggered.connect(self.close)
        file.addAction(exitMe)
        self.setStatusBar(QStatusBar(self))


app = QApplication([])
w = Fenster()
w.show()
app.exec()

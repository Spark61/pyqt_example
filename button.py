from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("erstes Programm")
        but = QPushButton("drück mich")
        but.setCheckable(True)
        but.clicked.connect(self.but_was_clicked)
        self.setCentralWidget(but)

    def but_was_clicked(self, info):
        print("clicked", info)

app = QApplication([])
win = MainWindow()
win.show()
app.exec()
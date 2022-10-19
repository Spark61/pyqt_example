import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formular App")
        self.label = QLabel("gib was ein")
        self.label.setWordWrap(True)
        font1 = self.label.font()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()

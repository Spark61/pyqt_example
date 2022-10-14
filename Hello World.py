import random
import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formular App")
        self.label = QLabel("BOX LAYOUT!")
        self.label.setWordWrap(True)
        font1 = self.label.font()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.button = QPushButton("Drück mich :)")
        self.button.clicked.connect(self.click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def click(self):
        print("Hello World")

        text = self.label.text()
        self.label.setText("")

        for key in list(text):
            if random.randint(0, 1) == 1:
                key = key.upper()
            else:
                key = key.lower()

            self.label.setText(self.label.text() + key)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()